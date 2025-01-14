import dash
from dash import html, dcc

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
import feffery_antd_charts as fact

from dash.dependencies import Input, Output, State

from server import app

from dashboard_c import *


data = [
    {"lastvalue": 1, "name": "11.88数据备份"},
    {"lastvalue": 2, "name": "2Zabbix server"},
    {"lastvalue": 3, "name": "31.70 VPN服务器"},
    {"lastvalue": 4, "name": "41.55 MES&APS 同步"},
    {"lastvalue": 5, "name": "5桃子园核心交换机1"},
]


def render():
    return [
        fac.AntdTitle("房屋受损情况", level=5),
        fact.AntdBar(
            id="bar",
            data=data,
            xField="lastvalue",
            yField="name",
            xAxis={"label": None},
            minBarWidth=20,
            maxBarWidth=20,
            height=250,
        ),
        fact.AntdColumn(
            data=data, xField="name", yField="lastvalue", xAxis={"label": None}, height=250
        ),
    ]
