from dash import html

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style


def render():
    return [
        fac.AntdFlex(
            [
                fac.AntdFlex(
                    [
                        fac.AntdTitle("本应用仅为技术测试", level=5),
                        fac.AntdText("数据定时抓取, 非实时消息, 仅供参考"),
                        fac.AntdTitle("欢迎关注公众号交流", level=5),
                        fac.AntdImage(
                            src="/assets/qrcode.png",
                            style=style(width="250px"),
                        ),
                        fac.AntdFlex(
                            [
                                fac.AntdTitle("项目地址:", level=5),
                                html.A(
                                    "Github-GHSLAB/california-fire-maps-dash",
                                    href="https://github.com/GHSLAB/california-fire-maps-dash",
                                ),
                            ],
                            vertical=True,
                        ),
                        ##
                        fac.AntdFlex(
                            [
                                fac.AntdTitle("Power by:", level=5),
                                html.A(
                                    "Python - Dash",
                                    href="https://dash.plotly.com/",
                                ),
                                html.A(
                                    "feffery-antd-components",
                                    href="https://fac.feffery.tech/",
                                ),
                                html.A(
                                    "feffery-antd-charts",
                                    href="https://fact.feffery.tech/",
                                ),
                                html.A(
                                    "feffery-leaflet-components",
                                    href="https://flc.feffery.tech/LeafletMap-basic",
                                ),
                                html.A(
                                    "feffery_utils_components",
                                    href="https://fuc.feffery.tech/",
                                ),
                            ],
                            vertical=True,
                        ),
                        ##
                        fac.AntdFlex(
                            [
                                fac.AntdTitle("Data Source:", level=5),
                                html.A(
                                    "github cbs-news-data",
                                    href="https://cbs-news-data.github.io/socal-fire-evacs_maplibre/",
                                ),
                                html.A(
                                    "Southern California Fires January 2025",
                                    href="https://calfire-forestry.maps.arcgis.com/home/item.html?id=0a7381c8b46b4e26a057383424f32c06",
                                ),
                                html.A(
                                    "https://www.fire.ca.gov",
                                    href="https://www.fire.ca.gov",
                                ),
                                html.A(
                                    "https://hub.wftiic.ca.gov",
                                    href="https://hub.wftiic.ca.gov",
                                ),
                                html.A(
                                    "https://protect.genasys.com/hazards",
                                    href="https://protect.genasys.com/hazards",
                                ),
                                html.A(
                                    "https://storms.ngs.noaa.gov",
                                    href="https://storms.ngs.noaa.gov/storms/2025_eri/index.html",
                                ),
                            ],
                            vertical=True,
                        ),
                    ],
                    vertical=True,
                )
            ],
            justify="center",
            style=style(width="100%", maxHeight="80%", overflowY="auto"),
        ),
    ]
