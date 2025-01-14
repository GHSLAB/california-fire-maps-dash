import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

import geopandas as gpd
import json

from config import MapConfig


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)


cbs_fire = read_json_file("./data/latest/cbs/latest_cali_fires.geojson")
cbs_evac = read_json_file("./data/latest/cbs/latest_cali_evac.geojson")

gdf_cbs_evac = gpd.GeoDataFrame.from_features(cbs_evac)
gdf_cbs_evac["category"] = gdf_cbs_evac["status"]

# 当使用 gdf.to_json() 生成 JSON 数据时，如果输出的字符串中带有反斜杠（\）
# 这是因为生成的 JSON 数据被转义了。默认情况下，to_json() 方法返回的是一个字符串
# 而字符串中的特殊字符（如引号 "）会被转义为 \"，因此会出现反斜杠。

gdf_cbs_evac_json = json.loads(gdf_cbs_evac.to_json())

write_json_file("gdf_cbs_evac_json.json", gdf_cbs_evac_json)


def basemap():
    return [
        flc.LeafletTileLayer(
            url=MapConfig.arcgis_imagery,
            zIndex=1,
        ),
        flc.LeafletTileLayer(
            url=MapConfig.labels,
            zIndex=10,
        ),
    ]


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
        center=center,
        zoom=zoom_level,
        style={"height": height},
    )


def render():
    return [
        fac.AntdFlex(
            [
                flc.LeafletMap(
                    basemap()
                    + [
                        flc.LeafletGeoJSON(
                            id="cbs_fire",
                            data=cbs_fire,
                            hoverable=True,
                            defaultStyle={
                                "color": "#c0392b",
                                "weight": 2,
                                "opacity": 1,
                                "fillColor": "#c0392b",
                                "fillOpacity": 0.2,
                            },
                            hoverStyle={
                                "fillOpacity": 0.2,
                                "color": "white",
                                "weight": 3,
                            },
                            fitBounds=False,
                        ),
                        flc.LeafletGeoJSON(
                            id="cbs_evac",
                            # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                            data=json.loads(gdf_cbs_evac.to_json()),
                            fitBounds=False,
                            mode="category",
                            featureCategoryToStyles={
                                "Evacuation Warning": {
                                    "color": "#d29200",
                                    "fillOpacity": 0.33,
                                    "weight": 1,
                                },
                                "Evacuation Order": {
                                    "color": "#ffb900",
                                    "fillOpacity": 0.33,
                                    "weight": 1,
                                },
                            },
                        ),
                    ],
                    center=[34.23595125, -118.3577035],  # -118.3577035, 34.23595125
                    zoom=10,
                    style={"height": "500px"},
                ),
                # leaflet_render(center=[34.198507, -118.139684], zoom_level=10, height="500px"),
            ],
            vertical=True,
        )
    ]
