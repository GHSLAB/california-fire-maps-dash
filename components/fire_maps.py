import dash
from dash import html

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

import geopandas as gpd
import json

# 配置
from config import MapConfig
from maps.legend import Legend
from maps.basemap import Basemap


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
# 而字符串中的特殊字符（如引号 "）会被转义为 \"，因此会出现反斜杠


cbs_style = {
    "Evacuation Warning": {
        "color": "#fd8724",
        "fillOpacity": 0.2,
        "weight": 1,
    },
    "Evacuation Order": {
        "color": "#820415",
        "fillOpacity": 0.2,
        "weight": 1,
    },
}


def render():
    return html.Div(
        [
            html.Div(
                flc.LeafletMap(
                    [
                        Basemap.arcgis_img(),
                        Basemap.light_labels(),
                        flc.LeafletLayerGroup(
                            flc.LeafletGeoJSON(
                                id="cbs_evac",
                                # 使用json.loads()将gdf.to_json字符串转换为JSON格式
                                data=json.loads(gdf_cbs_evac.to_json()),
                                fitBounds=False,
                                mode="category",
                                featureCategoryToStyles=cbs_style,
                            )
                        ),
                    ],
                    center=MapConfig.cal_center,
                    zoom=9,
                    style=style(height="400px", borderRadius="10px"),
                ),
                style=style(height="400px", borderRadius="30px"),
            ),
            # fac.AntdText("Source: CalFire"),
            fac.AntdSpace(
                [
                    fac.AntdCheckbox(id="cbs_evac_check", label="疏散数据", checked=True),
                    Legend.fill("疏散命令", "#820415"),
                    Legend.fill("疏散警告", "#fd8724"),
                ],
                style=style(marginTop="5px"),
            ),
        ],
    )
