from dash import html

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style


def render():
    return [
        fac.AntdCenter(
            fac.AntdFlex(
                [
                    fac.AntdTitle("本应用仅为技术测试", level=5),
                    fac.AntdText("数据定时抓取, 非实时消息, 仅供参考"),
                    fac.AntdDivider(style=style(marginTop="5px", marginBottom="5px")),
                    fac.AntdTitle("欢迎关注公众号交流", level=5),
                    fac.AntdImage(
                        src="/assets/qrcode.png",
                        style=style(width="250px"),
                    ),
                    fac.AntdDivider(),
                    fac.AntdText("项目地址:"),
                    html.A(
                        "Github-GHSLAB/california-fire-maps-dash",
                        href="https://github.com/GHSLAB/california-fire-maps-dash",
                    ),
                    html.Pre(
                        [
                            fac.AntdTitle("Power by:", level=5),
                            fac.AntdText("Python - Dash"),
                            fac.AntdText("feffery-antd-components"),
                            fac.AntdText("feffery-antd-charts"),
                            fac.AntdText("feffery-leaflet-components"),
                            fac.AntdText("feffery_utils_components"),
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
                        ]
                    ),
                ],
                vertical=True,
            ),
            style=style(width="100%", padding="10px"),
        ),
    ]
