import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style

damage_pic_list = []


def render():
    return [
        fac.AntdCarousel(
            [
                fac.AntdCenter(
                    i,
                    style={
                        "color": "white",
                        "fontSize": 36,
                        "height": 160,
                        "backgroundColor": "#364d79",
                    },
                )
                for i in range(1, 6)
            ],
            effect="fade",
        )
    ]
