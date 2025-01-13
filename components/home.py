import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style


def render():
    return [
        fac.AntdFlex(
            [
                fac.AntdImage(
                    src="/assets/imagery/fire.webp",
                    style={"width": "100%"},
                ),
                fac.AntdText("Source: The Associated Press/Maxar Technologies"),
                fac.AntdText("2025.1.8 Wednesday"),
            ],
            vertical=True,
        )
    ]
