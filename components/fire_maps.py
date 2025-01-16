import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output, State, ALL, MATCH

import geopandas as gpd
import json

from maps.basemap import Basemap

from config import MapConfig
from server import app


def split_map_render():
    return [
        flc.LeafletMapProvider(
            fac.AntdCol(
                [
                    fac.AntdRow(
                        flc.LeafletMap(
                            [
                                Basemap.light_labels(),
                                flc.LeafletTileLayer(
                                    url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                                ),
                                Basemap.light_labels(),
                                flc.LeafletMapSync(id="split-map1"),
                            ],
                            center={"lng": -118.46965, "lat": 34.04239},  # 34.04239/-118.46965
                            zoom=12,
                            style=style(
                                height=299,
                                width="100%",
                                # borderbottom="2px solid white;",
                            ),
                        ),
                    ),
                    fac.AntdRow(
                        flc.LeafletMap(
                            [
                                Basemap.light_labels(),
                                flc.LeafletTileLayer(
                                    url="https://stormscdn.ngs.noaa.gov/20250114m-maxar/{z}/{x}/{y}",
                                    zIndex=99,
                                ),
                                flc.LeafletTileLayer(
                                    url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                                    zIndex=1,
                                    opacity=0.5,
                                ),
                                flc.LeafletMapSync(id="split-map2"),
                            ],
                            center={"lng": -118.46965, "lat": 34.04239},  # 34.04239/-118.46965
                            zoom=12,
                            zoomControl=False,
                            style=style(
                                height=299,
                                width="100%",
                                marginTop="2px",
                                # borderTop="1px solid white;",
                            ),
                        ),
                    ),
                ],
                style={"height": 600, "width": "100%"},
            )
        )
    ]


def rolling_map_render():
    return [
        flc.LeafletMapProvider(
            fuc.FefferyCompareSlider(
                firstItem=flc.LeafletMap(
                    [
                        flc.LeafletTileLayer(
                            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                        ),
                        flc.LeafletMapSync(id="split-map1"),
                    ],
                    center={"lng": -118.46965, "lat": 34.04239},  # 34.04239/-118.46965
                    zoom=12,
                    style={"height": 600},
                ),
                secondItem=flc.LeafletMap(
                    [
                        flc.LeafletTileLayer(
                            url="https://stormscdn.ngs.noaa.gov/20250114m-maxar/{z}/{x}/{y}",
                            zIndex=99,
                        ),
                        flc.LeafletTileLayer(
                            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                            zIndex=1,
                            opacity=0.5,
                        ),
                        flc.LeafletMapSync(id="split-map2"),
                    ],
                    center={"lng": -118.46965, "lat": 34.04239},
                    zoom=12,
                    style={"height": 600},
                ),
                style={"zIndex": 999},
            )
        ),
    ]


#
maxar_time = ["2025-01-08", "2025-01-09", "2025-01-10", "2025-01-13", "2025-01-14"]
maxar_date = ["01-08", "01-09", "01-10", "01-13", "01-14"]


# 主页面
def render():
    return [
        fuc.FefferyStyle(  # 提升卷帘拖拽条z-index
            rawStyle="""
[data-rcs="handle-container"] {
    z-index: 500;
}
"""
        ),
        fac.AntdSpace(
            [
                fac.AntdButton("卷帘模式", type="primary", id="rolling-mode"),
                fac.AntdButton("分屏模式", id="split-mode"),
                fac.AntdText("切片服务加载较慢", style=style(position="absolute", right="5px")),
            ],
            direction="horizontal",
        ),
        html.Div(
            rolling_map_render(),
            id="map-container",
            style=style(marginTop=10, borderRadius=15),
        ),
        fac.AntdFlex(
            [fac.AntdText("数据源: ArcGIS/MAXAR"), fac.AntdText("时间:2025-01-14")],
            justify="space-between",
            style=style(margin=3),
        ),
        # fac.AntdFlex(
        #     [
        #         fac.AntdButton(
        #             f"{date}",
        #             id={"type": "button", "index": date},
        #             type="primary" if date == "01-14" else "default",
        #         )
        #         for date in maxar_date
        #     ],
        #     vertical=False,
        #     justify="space-around",
        #     style=style(marginTop=10),
        # ),
        # fac.AntdSteps(
        #     steps=[
        #         {
        #             "title": f"步骤{i + 1}",
        #         }
        #         for i in range(5)
        #     ],
        #     labelPlacement="vertical",
        # ),
        # fac.AntdSegmented(
        #     options=[
        #         {"label": "01-14", "value": "0114"},
        #         {"label": "01-13", "value": "0113"},
        #         {"label": "01-10", "value": "0110"},
        #         {"label": "01-09", "value": "0109"},
        #         {"label": "01-08", "value": "0108"},
        #     ],
        #     size="large",
        #     defaultValue="0114",
        # ),
    ]


@app.callback(
    [
        Output("split-mode", "type", allow_duplicate=True),
        Output("rolling-mode", "type", allow_duplicate=True),
        Output("map-container", "children", allow_duplicate=True),
    ],
    Input("split-mode", "nClicks"),
    prevent_initial_call=True,
)
def split_mode(nClicks):
    if nClicks:
        return ["primary", "default", split_map_render()]


@app.callback(
    [
        Output("split-mode", "type", allow_duplicate=True),
        Output("rolling-mode", "type", allow_duplicate=True),
        Output("map-container", "children", allow_duplicate=True),
    ],
    Input("rolling-mode", "nClicks"),
    prevent_initial_call=True,
)
def rolling_mode(nClicks):
    if nClicks:
        return ["default", "primary", rolling_map_render()]

    # return [
    #     fuc.FefferyCompareSlider(
    #         firstItem=flc.LeafletMap(
    #             [Basemap.arcgis_imgery()],
    #             center=MapConfig.deafult_center,
    #             zoom=12,
    #             zoomControl=False,
    #             style={"width": 800, "height": 500},
    #         ),
    #         secondItem=flc.LeafletMap(
    #             [
    #                 flc.LeafletTileLayer(
    #                     url="https://stormscdn.ngs.noaa.gov/20250114m-maxar/{z}/{x}/{y}"
    #                 )
    #             ],
    #             center=MapConfig.deafult_center,
    #             zoom=12,
    #             zoomControl=False,
    #             style={"width": 800, "height": 500},
    #         ),
    #         style={"width": 800, "height": 500},
    #     ),
    # ]
