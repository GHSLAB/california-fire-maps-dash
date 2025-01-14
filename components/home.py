import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style


import json


def render():
    return [
        fac.AntdFlex(
            [
                # cal_fire.render(),
                # leaflet_render(center=[34.198507, -118.139684], zoom_level=10, height="500px"),
            ],
            vertical=True,
        )
    ]
