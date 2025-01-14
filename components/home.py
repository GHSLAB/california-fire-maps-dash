import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style

from config import MapConfig


def leaflet_render(center: tuple, zoom_level: int, height: str):
    return flc.LeafletMap(
        [
            flc.LeafletTileLayer(
                url=MapConfig.arcgis_imagery,
                zIndex=1,
            ),
            flc.LeafletTileLayer(
                url=MapConfig.labels,
                zIndex=10,
            ),
        ],
        center=center,  # [34.198507, -118.139684]
        zoom=zoom_level,
        style={"height": height},
    )


def render():
    return [
        fac.AntdFlex(
            [
                fac.AntdImage(
                    src="/assets/rs/maxar.webp",
                    style={"width": "100%"},
                ),
                fac.AntdText("Source: The Associated Press/Maxar Technologies"),
                fac.AntdText("2025.1.8 Wednesday"),
                leaflet_render(center=[34.198507, -118.139684], zoom_level=10, height="300px"),
            ],
            vertical=True,
        )
    ]
