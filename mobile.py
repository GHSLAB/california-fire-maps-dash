import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style

from components import home, imagery_compare, timeline, about


def render():
    return [
        fac.AntdTitle("Los Angeles Wildfire", level=4, style={"margin": "5px"}),
        fac.AntdTitle("Satellite Imagery Comparison", level=4, style={"margin": "5px"}),
        # fac.AntdTitle("洛杉矶山火影像对比", level=4, style={"margin": "5px"}),
        fac.AntdTabs(
            items=[
                {
                    "key": "主页",
                    "label": "主页",
                    "children": home.render(),
                },
                {
                    "key": "数据",
                    "label": "数据",
                    "children": imagery_compare.render(),
                },
                {
                    "key": "影像",
                    "label": "影像",
                    "children": imagery_compare.render(),
                },
                {
                    "key": "时间线",
                    "label": "时间线",
                    "children": timeline.render(),
                },
                {
                    "key": "参考",
                    "label": "参考",
                    "children": home.render(),
                },
                {
                    "key": "关于",
                    "label": "关于",
                    "children": about.render(),
                },
            ],
            type="card",
            centered=True,
        ),
    ]
