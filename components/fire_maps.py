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
from maps import tile_selector


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)


cbs_fire = read_json_file("./data/latest/cbs/latest_cali_fires.geojson")
cbs_evac = read_json_file("./data/latest/cbs/latest_cali_evac.geojson")

gdf_cbs_evac = gpd.GeoDataFrame.from_features(cbs_evac)
gdf_cbs_evac["category"] = gdf_cbs_evac["status"]

# 当使用 gdf.to_json() 生成 JSON 数据时，如果输出的字符串中带有反斜杠（\）
# 这是因为生成的 JSON 数据被转义了。默认情况下，to_json() 方法返回的是一个字符串
# 而字符串中的特殊字符（如引号 "）会被转义为 \"，因此会出现反斜杠


cbs_style = {
    "Evacuation Warning": {
        "color": "#fd8724",
        "fillColor": "#fd8724",
        "fillOpacity": 0.2,
        "weight": 1,
    },
    "Evacuation Order": {
        "color": "#820415",
        "fillColor": "#820415",
        "fillOpacity": 0.2,
        "weight": 1,
    },
}


def render():
    return html.Div(
        [
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            # Basemap.arcgis_img(),
                            flc.LeafletTileLayer(id="tile-layer", zIndex=1, opacity=0.8),
                            Basemap.light_labels(),
                            flc.LeafletLayerGroup(  # evac order
                                flc.LeafletGeoJSON(
                                    # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                                    data=json.loads(
                                        gdf_cbs_evac[
                                            gdf_cbs_evac["status"] == "Evacuation Order"
                                        ].to_json()
                                    ),
                                    defaultStyle=cbs_style["Evacuation Order"],
                                    fitBounds=False,
                                    # mode="category",
                                    # featureCategoryToStyles=cbs_style,
                                    hoverable=True,
                                ),
                                id="cbs_evac_order",
                                hidden=False,
                                zIndex=100,
                            ),
                            flc.LeafletLayerGroup(  # evac warning
                                flc.LeafletGeoJSON(
                                    # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                                    data=json.loads(
                                        gdf_cbs_evac[
                                            gdf_cbs_evac["status"] == "Evacuation Warning"
                                        ].to_json()
                                    ),
                                    defaultStyle=cbs_style["Evacuation Warning"],
                                    fitBounds=False,
                                    # mode="category",
                                    # featureCategoryToStyles=cbs_style,
                                    hoverable=True,
                                ),
                                id="cbs_evac_warning",
                                hidden=False,
                                zIndex=50,
                            ),
                            flc.LeafletLayerGroup(),
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
            # fac.AntdText("Source: CalFire"),
            fac.AntdSpace(
                [
                    fac.AntdSpace(
                        [
                            fac.AntdCheckbox(id="cbs_evac_check", label="疏散区域", checked=True),
                            Legend.fill("疏散命令", "#820415"),
                            Legend.fill("疏散警告", "#fd8724"),
                        ],
                        direction="horizontal",
                        style=style(marginTop="5px"),
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdCheckbox(
                                id="burned_area_check", label="受灾区域", checked=False
                            ),
                            Legend.fill("疏散命令", "#820415"),
                            # Legend.fill("疏散警告", "#fd8724"),
                        ],
                    ),
                ],
                direction="vertical",
            ),
        ],
    )


# 图层控制
@dash.callback(
    [Output("cbs_evac_order", "hidden"), Output("cbs_evac_warning", "hidden")],
    Input("cbs_evac_check", "checked"),
)
def cbs_evac_check(checked):
    if checked:
        return [False, False]
    else:
        return [True, True]
