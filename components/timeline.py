import dash
from dash import html, dcc

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output, State

import json

from server import app


def get_timeline_item(timeline_file: str) -> dict:
    with open(timeline_file, "r", encoding="utf-8") as file:
        timeline = json.load(file)
    item_dict = []
    for i in reversed(timeline):
        item_dict.append(
            {
                "content": fac.AntdFlex(
                    [
                        fac.AntdText(f"{i['time']}", style=style(fontWeight="bold")),
                        fac.AntdText(f"{i['content']}"),
                    ],
                    vertical=True,
                )
            }
        )
    return item_dict


def get_json_config(timeline_file: str, column: str) -> str:
    with open(timeline_file, "r", encoding="utf-8") as file:
        data = json.load(file)[0]
    return data[f"{column}"]


# timeline
def timeline():
    return get_timeline_item("./data/forbes/timeline.json")


def update_time():
    return get_json_config("./data/forbes/update_time.json", "Last updated")


def timeline_cn():
    return get_timeline_item("./data/forbes/timeline_cn.json")


def translate_time():
    return get_json_config("./data/forbes/translate_time.json", "Last updated")


def render():
    return [
        html.Div(id="refresh-status"),
        html.Div(
            [
                fac.AntdSpace(
                    fac.AntdFlex(
                        [
                            fac.AntdButton(
                                "翻转",
                                id="switch-timeline",
                                disabled=False,
                                type="primary",
                                style=style(marginLeft="5px"),
                            ),
                            fac.AntdButton(
                                fac.AntdIcon(
                                    icon="md-translate",
                                ),
                                id="language-switch",
                                variant="text",
                                color="default",
                                style=style(
                                    position="absolute", right="10px", width="32px", height="32px"
                                ),
                            ),
                        ],
                    ),
                    direction="horizontal",
                    size="large",
                    style=style(marginBottom="15px"),
                ),
                html.Div(
                    [
                        # fac.AntdSpin(fac.AntdText(id="spin-refresh"), text="数据获取中"),
                        fac.AntdSpace(
                            fac.AntdTimeline(
                                id="timeline", pending="NOW", items=timeline(), reverse=True
                            )
                        ),
                    ],
                    id="back-top-container-demo",
                    style={
                        "height": "calc(100vh - 300px)",
                        "maxHeight": "calc(100vh - 300px)",
                        "overflowY": "auto",
                        "position": "relative",
                        "backgroundColor": "rgba(240, 240, 240, 0.5)",
                        "borderRadius": "5px",
                        "boxShadow": "0 0 10px rgba(0, 0, 0, 0.3)",
                        "border": "1px solid #f0f0f0",
                        "padding": "20px",
                    },
                ),
                fac.AntdBackTop(
                    containerId="back-top-container-demo",
                    duration=1,
                    style=style(zIndex=1000),
                ),
                fac.AntdFlex(
                    [
                        fac.AntdText(
                            f"更新时间: {update_time()}",
                            id="update-time",
                            style=style(marginLeft="5px"),
                        ),
                        html.A(
                            "from Forbes",
                            href="https://www.forbes.com/sites/antoniopequenoiv/2025/01/12/california-wildfire-live-updates-death-toll-hits-24-in-palisades-eaton-fires-as-heavy-wind-expected-in-coming-days/",
                            style=style(position="absolute", right="15px", color="#8B8B8B"),
                        ),
                    ],
                    style=style(paddingTop="10px"),
                ),
            ],
            style=style(margin="0 10px 10px 10px"),
        ),
    ]


# 回调


# 切换方向
@app.callback(
    Output("timeline", "reverse", allow_duplicate=True),
    Input("switch-timeline", "nClicks"),
    State("timeline", "reverse"),
    prevent_initial_call=True,
)
def switch_timeline(nClicks, reverse):
    if nClicks:
        if reverse is False:
            return True
        else:
            return False


# 切换翻译
@app.callback(
    [
        Output("timeline", "items", allow_duplicate=True),
        Output("update-time", "children", allow_duplicate=True),
    ],
    Input("language-switch", "nClicks"),
    prevent_initial_call=True,
)
def switch_language(nClicks):
    if nClicks:
        # 计算nClicks是否为单数
        is_odd = nClicks % 2 != 0
        if is_odd:
            return [timeline_cn(), f"翻译时间: {translate_time()}"]
        else:
            return [timeline(), f"更新时间: {update_time()}"]
