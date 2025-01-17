import dash
from dash import html

import feffery_antd_components as fac


from feffery_dash_utils.style_utils import style

from components import home, fire_maps, dashboard, timeline, about


def render():
    return html.Div(
        [
            html.Div(
                [
                    fac.AntdFlex(
                        fac.AntdTitle("2025 加州山火地图", level=4, style={"margin": "0px"}),
                        justify="center",
                    ),
                    fac.AntdFlex(
                        fac.AntdTitle("California Fire Map", level=4, style={"margin": "0px"}),
                        justify="center",
                    ),
                ],
                # style=style(height="15%"),
            ),
            fac.AntdTabs(
                items=[
                    {
                        "key": "homepage",
                        "label": "主页",
                        "children": home.render(),
                    },
                    {
                        "key": "资讯",
                        "label": "资讯",
                        "children": timeline.render(),
                    },
                    {
                        "key": "maps",
                        "label": "卫星影像",
                        "children": fire_maps.render(),
                    },
                    {
                        "key": "stats",
                        "label": "数据统计",
                        "children": dashboard.render(),
                    },
                    {
                        "key": "about",
                        "label": "关于",
                        "children": about.render(),
                    },
                ],
                defaultActiveKey="homepage",
                tabPosition="top",
                centered=True,
                style=style(width="100%", overflowY="auto"),
            ),
        ],
        style=style(width="100%"),
    )
