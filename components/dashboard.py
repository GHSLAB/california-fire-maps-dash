import dash
from dash import html, dcc

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
import feffery_antd_charts as fact

from dash.dependencies import Input, Output, State

import json
import geopandas as gpd

from server import app


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


## CBS 数据
cbs_fire = read_json_file("./data/latest/cbs/latest_cali_fires.geojson")

gdf_cbs_fire = gpd.GeoDataFrame.from_features(cbs_fire)
gdf_cbs_fire["烧毁面积(km2)"] = round(gdf_cbs_fire["acres_burned"] * 0.00404686, 2)

data = (
    gdf_cbs_fire[["fire_name", "烧毁面积(km2)"]]
    .sort_values(by="烧毁面积(km2)", ascending=False)
    .to_dict("records")
)

chart_style = {
    "backgroundColor": "rgba(240, 240, 240, 0.5)",
    "border": "2px solid #ccc",
    "borderRadius": "10px",
    "boxShadow": "0 5 10px rgba(0, 0, 0, 0.5)",
}


def render():
    return [
        fac.AntdTitle("烧毁面积", level=5, className="subtitle"),
        html.Div(
            fact.AntdBar(
                id="bar",
                data=data,
                xField="烧毁面积(km2)",
                yField="fire_name",
                label={"position": "right"},
                minBarWidth=20,
                maxBarWidth=25,
                height=250,
                style=style(padding="10px"),
            ),
            style=chart_style,
        ),
    ]
