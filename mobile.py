import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style

from components import home, fire_maps, dashboard, imagery, timeline, about


def render():
    return [
        fac.AntdFlex(
            fac.AntdTitle("2025 加州山火地图", level=4, style={"margin": "0px"}), justify="center"
        ),
        fac.AntdFlex(
            fac.AntdTitle("California Fire Map", level=4, style={"margin": "0px"}), justify="center"
        ),
        fac.AntdTabs(
            items=[
                {
                    "key": "主页",
                    "label": "主页",
                    "children": home.render(),
                },
                {
                    "key": "地图",
                    "label": "地图",
                    "children": fire_maps.render(),
                },
                {
                    "key": "数据",
                    "label": "数据",
                    "children": dashboard.render(),
                },
                {
                    "key": "资讯",
                    "label": "资讯",
                    "children": timeline.render(),
                },
                {
                    "key": "画廊",
                    "label": "画廊",
                    "children": imagery.render(),
                },
                {
                    "key": "关于",
                    "label": "关于",
                    "children": about.render(),
                },
            ],
            defaultActiveKey="数据",
            # type="card",
            centered=True,
            # style={"marginTop": "5px"},
        ),
    ]
