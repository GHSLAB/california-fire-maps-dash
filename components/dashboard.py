import dash
from dash import html, dcc

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
import feffery_antd_charts as fact

from dash.dependencies import Input, Output, State


from server import app

from models.gpd_data import cbsdata, arcgisdata

chart_style = {
    "backgroundColor": "rgba(240, 240, 240, 0.5)",
    "border": "0px solid #ccc",
    "borderRadius": "10px",
    "boxShadow": "inset 0 0 5px rgba(0, 0, 0, 0.5)",
}


def render():
    return html.Div(
        [
            fac.AntdTitle("烧毁面积", level=5, className="subtitle1"),
            html.Div(
                fact.AntdBar(
                    id="burn-area",
                    data=cbsdata.burn_area_dict(),
                    xField="烧毁面积(km2)",
                    yField="fire_name",
                    label={"position": "right"},
                    xAxis={"max": 120},
                    minBarWidth=20,
                    maxBarWidth=25,
                    height=250,
                    style=style(padding="10px"),
                ),
                style=chart_style,
            ),
            fac.AntdTitle("救灾投入", level=5, className="subtitle1"),
            html.Div(
                fact.AntdColumn(
                    id="save-resoucres",
                    data=arcgisdata.save_resoucres_dict(),
                    xField="类型",
                    yField="数量",
                    yAxis={"max": 750},
                    seriesField="名称",
                    label={"position": "top"},
                    legend={"position": "top-right"},
                    isGroup=True,
                    minColumnWidth=25,
                    # legend=True,
                    height=200,
                    style=style(padding="10px"),
                ),
                style=chart_style,
            ),
            fac.AntdTitle("人员伤亡", level=5, className="subtitle1"),
            html.Div(
                fact.AntdColumn(
                    id="casualties",
                    data=arcgisdata.casualties_dict(),
                    xField="类型",
                    yField="数量",
                    yAxis={"max": 20},
                    seriesField="名称",
                    label={"position": "top"},
                    legend={"position": "top-right"},
                    isGroup=True,
                    minColumnWidth=15,
                    maxColumnWidth=30,
                    height=200,
                    style=style(padding="10px"),
                ),
                style=chart_style,
            ),
        ],
        style=style(padding="10px"),
    )
