import dash
from dash import html, dcc

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style


def render():
    return [
        fac.AntdCenter(
            fac.AntdFlex(
                [
                    fac.AntdTitle("本应用仅为技术测试, 信息仅供参考", level=4),
                    fac.AntdText("欢迎扫码关注公众号交流"),
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
                    fac.AntdDivider(),
                    fac.AntdTitle("Powerby:", level=5),
                    fac.AntdText("feffery-antd-components"),
                ],
                vertical=True,
            )
        ),
        html.Div(
            [
                fac.AntdDivider(
                    style=style(marginBottom="10px"),
                ),
                fac.AntdFlex(
                    [
                        fac.AntdCenter(
                            html.A(
                                "闽ICP备2023008814号-3",
                                href="https://beian.miit.gov.cn/",
                                style=style(fontSize="12px", color="#8B8B8B"),
                            ),
                        ),
                    ],
                    vertical=True,
                    style=style(marginBottom="10px"),
                ),
            ],
            style=style(position="fixed", bottom="0", width="100%"),
        ),
    ]
