# dash
import dash
from dash import html

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output


# 配置
from server import app
from config import MapConfig

# 地图组件
from maps.legend import Legend
from maps.basemap import Basemap
from maps import tile_selector, symbol_style

# 数据
from models.gpd_data import cbsdata, arcgisdata


def render():
    return html.Div(
        [
            html.Div(
                [
                    flc.LeafletMap(
                        [
                            flc.LeafletTileLayer(id="tile-layer", zIndex=1, opacity=0.8),
                            Basemap.light_labels(),
                            flc.LeafletLayerGroup(  # cbs_fire
                                flc.LeafletGeoJSON(
                                    data=cbsdata.fire_gdf_to_json(),
                                    defaultStyle=symbol_style.cbs.Fire,
                                    fitBounds=False,
                                    showTooltip=True,
                                    featureTooltipField="fire_name",
                                    hoverable=True,
                                ),
                                id="cbs_fire",
                                hidden=False,
                                zIndex=9999,
                            ),
                            flc.LeafletLayerGroup(  # evac order
                                flc.LeafletGeoJSON(
                                    data=cbsdata.evac_order_gdf_to_json(),
                                    defaultStyle=symbol_style.cbs.Evacuation_Order,
                                    fitBounds=False,
                                    showTooltip=True,
                                    featureTooltipField="status",
                                    hoverable=True,
                                ),
                                id="cbs_evac_order",
                                hidden=True,
                                # zIndex=100,
                            ),
                            flc.LeafletLayerGroup(  # evac warning
                                flc.LeafletGeoJSON(
                                    data=cbsdata.evac_warning_gdf_to_json(),
                                    defaultStyle=symbol_style.cbs.Evacuation_Warning,
                                    fitBounds=False,
                                    showTooltip=True,
                                    featureTooltipField="status",
                                    hoverable=True,
                                ),
                                id="cbs_evac_warning",
                                hidden=True,
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
                    fac.AntdText(f"{cbsdata.evac_timestamp()} PST", style=style(marginLeft="5px")),
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
                            fac.AntdCheckbox(id="burned_area_check", checked=True),
                            Legend.fill("烧毁区域", symbol_style.cbs.Fire["fillColor"]),
                            fac.AntdCheckbox(
                                id="cbs_evac_order_check",
                                checked=False,
                            ),
                            Legend.fill(
                                "疏散命令",
                                symbol_style.cbs.Evacuation_Order["fillColor"],
                            ),
                            fac.AntdCheckbox(
                                id="cbs_evac_warning_check",
                                checked=False,
                            ),
                            Legend.fill(
                                "疏散警告", symbol_style.cbs.Evacuation_Warning["fillColor"]
                            ),
                        ],
                        style=style(marginTop="5px"),
                    ),
                ],
                direction="vertical",
            ),
            fac.AntdTable(
                columns=[
                    {"title": "区域", "dataIndex": "name"},
                    {"title": "起火时间(UTC)", "dataIndex": "起火时间"},
                    {"title": "烧毁面积(km2)", "dataIndex": "烧毁面积"},
                    {
                        "title": "火势控制进度",
                        "dataIndex": "火势控制进度",
                        "renderOptions": {"renderType": "mini-progress"},
                        "width": "25%",
                    },
                ],
                data=arcgisdata.save_progress_dict(type="data"),
                style=style(marginTop="10px"),
            ),
        ],
    )


# 图层控制
@app.callback(
    Output("cbs_fire", "hidden"),
    Input("burned_area_check", "checked"),
)
def cbs_fire_check(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output("cbs_evac_order", "hidden"),
    Input("cbs_evac_order_check", "checked"),
)
def cbs_evac_order_check(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output("cbs_evac_warning", "hidden"),
    Input("cbs_evac_warning_check", "checked"),
)
def cbs_evac_warning_check(checked):
    if checked:
        return False
    else:
        return True
