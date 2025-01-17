# legend.py
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style


class Basemap:
    arcgis_imagery_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    light_only_labels = "https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png"

    @classmethod
    def arcgis_imgery(cls):
        return flc.LeafletTileLayer(url=cls.arcgis_imagery_url, zIndex=1)

    @classmethod
    def light_labels(cls):
        return flc.LeafletTileLayer(url=cls.light_only_labels, zIndex=9999)
