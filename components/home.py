import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output, State

import geopandas as gpd
import json

# 配置
from config import MapConfig
from maps.legend import Legend
from maps.basemap import Basemap
from maps import tile_selector, symbol_style


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)


## CBS 数据
gdf_cbs_fire = gpd.GeoDataFrame.from_features(
    read_json_file("./data/latest/cbs/latest_cali_fires.geojson")
)
gdf_cbs_evac = gpd.GeoDataFrame.from_features(
    read_json_file("./data/latest/cbs/latest_cali_evac.geojson")
)
cbs_data_time = gdf_cbs_evac["timestamp"].max()


# 将英亩转换为平方千米（1英亩约等于0.00404686平方千米）
gdf_cbs_fire["acres_burned_km2"] = gdf_cbs_fire["acres_burned"] * 0.00404686

# 更新tooltip列
gdf_cbs_fire["tooltip"] = (
    gdf_cbs_fire["fire_name"].astype(str)
    + "损毁面积"
    + gdf_cbs_fire["acres_burned_km2"].round(2).astype(str)
    + "平方千米"
)


def render():
    return html.Div(
        [
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            # Basemap.arcgis_imgery(),
                            flc.LeafletTileLayer(id="tile-layer", zIndex=1, opacity=0.8),
                            Basemap.light_labels(),
                            flc.LeafletLayerGroup(  # cbs_fire
                                flc.LeafletGeoJSON(
                                    # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                                    data=json.loads(gdf_cbs_fire.to_json()),
                                    defaultStyle=symbol_style.cbs.Fire,
                                    fitBounds=False,
                                    showTooltip=True,
                                    featureTooltipField="tooltip",
                                    hoverable=True,
                                    tooltipDirection="center",
                                ),
                                id="cbs_fire",
                                hidden=False,
                                zIndex=9999,
                            ),
                            flc.LeafletLayerGroup(  # evac order
                                flc.LeafletGeoJSON(
                                    # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                                    data=json.loads(
                                        gdf_cbs_evac[
                                            gdf_cbs_evac["status"] == "Evacuation Order"
                                        ].to_json()
                                    ),
                                    defaultStyle=symbol_style.cbs.Evacuation_Order,
                                    fitBounds=False,
                                    showTooltip=True,
                                    featureTooltipField="status",
                                    hoverable=True,
                                ),
                                id="cbs_evac_order",
                                hidden=False,
                                # zIndex=100,
                            ),
                            flc.LeafletLayerGroup(  # evac warning
                                flc.LeafletGeoJSON(
                                    # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                                    data=json.loads(
                                        gdf_cbs_evac[
                                            gdf_cbs_evac["status"] == "Evacuation Warning"
                                        ].to_json()
                                    ),
                                    defaultStyle=symbol_style.cbs.Evacuation_Warning,
                                    fitBounds=False,
                                    showTooltip=True,
                                    featureTooltipField="status",
                                    hoverable=True,
                                ),
                                id="cbs_evac_warning",
                                hidden=False,
                                # zIndex=50,
                            ),
                        ],
                        center=MapConfig.deafult_center,
                        zoom=9,
                        showMeasurements=True,
                        measureControl=True,
                        scaleControl=True,
                        style=style(height="400px", width="100%"),
                    ),
                    flc.LeafletTileSelect(  # 底图切换器
                        id="tile-select",
                        # 默认底图
                        selectedUrl=tile_selector.basemap[0]["url"],
                        # 底图url
                        urls=tile_selector.basemap,
                        containerVisible=False,
                        # 缩略图参数
                        center=MapConfig.deafult_center,
                        zoom=7,
                        style=style(
                            maxWidth="80%",
                        ),
                    ),
                ]
            ),
            fac.AntdFlex(
                [
                    fac.AntdText(
                        "数据时间",
                        style=style(fontWeight="bold"),
                    ),
                    fac.AntdText(f"{cbs_data_time} PST", style=style(marginLeft="5px")),
                    fac.AntdText(
                        "Source: CalFire",
                        style=style(position="absolute", right="5px", color="#8B8B8B"),
                    ),
                ],
                vertical=False,
            ),
            fac.AntdSpace(
                [
                    fac.AntdSpace(
                        [
                            fac.AntdText(
                                "受灾情况",
                                style=style(fontWeight="bold"),
                            ),
                            fac.AntdCheckbox(id="burned_area_check", checked=False),
                            Legend.fill("烧毁区域", symbol_style.cbs.Fire["fillColor"]),
                            # Legend.fill("疏散警告", "#fd8724"),
                        ],
                        style=style(marginTop="5px"),
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdText(
                                "疏散情况",
                                style=style(fontWeight="bold"),
                            ),
                            fac.AntdCheckbox(
                                id="cbs_evac_order_check",
                                checked=True,
                            ),
                            Legend.fill(
                                "疏散命令",
                                symbol_style.cbs.Evacuation_Order["fillColor"],
                            ),
                            # fac.AntdCheckbox(
                            #     id="cbs_evac_warning_check",
                            #     checked=True,
                            # ),
                            Legend.fill(
                                "疏散警告", symbol_style.cbs.Evacuation_Warning["fillColor"]
                            ),
                        ],
                        direction="horizontal",
                    ),
                ],
                direction="vertical",
            ),
            html.Div(style=style(height="150px", width="100%")),
        ],
    )


# 图层控制
@dash.callback(
    Output("cbs_fire", "hidden"),
    Input("burned_area_check", "checked"),
)
def cbs_fire_check(checked):
    if checked:
        return False
    else:
        return True


@dash.callback(
    [Output("cbs_evac_warning", "hidden"), Output("cbs_evac_order", "hidden")],
    Input("cbs_evac_order_check", "checked"),
)
def cbs_evac_order_check(checked):
    if checked:
        return [False, False]
    else:
        return [True, True]


# @dash.callback(
#     Output("cbs_evac_warning", "hidden"),
#     Input("cbs_evac_warning_check", "checked"),
# )
# def cbs_evac_warning_check(checked):
#     if checked:
#         return False
#     else:
#         return True
