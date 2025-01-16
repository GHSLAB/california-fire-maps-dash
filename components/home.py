# dash
import dash
from dash import html

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style
import feffery_antd_charts as fact

from dash.dependencies import Input, Output, State


# 配置
from config import MapConfig

# 地图组件
from maps.legend import Legend
from maps.basemap import Basemap
from maps import tile_selector, symbol_style

# 数据
from models.gpd_data import cbsdata, arcgisdata

from components.dashboard import chart_style


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
                            fac.AntdText(
                                "受灾情况",
                                style=style(fontWeight="bold"),
                            ),
                            fac.AntdCheckbox(id="burned_area_check", checked=True),
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
                        direction="horizontal",
                    ),
                ],
                direction="vertical",
                # style=style(height="150px", width="100%"),
            ),
            fac.AntdTitle("火势控制进度", level=5),
            html.Div(
                fact.AntdBar(
                    id="save_progress_chart",
                    data=arcgisdata.save_progress_dict(),
                    xField="火势控制进度",
                    yField="区域",
                    label={"position": "middle"},
                    minBarWidth=20,
                    maxBarWidth=25,
                    height=250,
                    style=style(padding="10px"),
                ),
                style=chart_style,
            ),
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
    Output("cbs_evac_order", "hidden"),
    Input("cbs_evac_order_check", "checked"),
)
def cbs_evac_order_check(checked):
    if checked:
        return False
    else:
        return True


@dash.callback(
    Output("cbs_evac_warning", "hidden"),
    Input("cbs_evac_warning_check", "checked"),
)
def cbs_evac_warning_check(checked):
    if checked:
        return False
    else:
        return True
