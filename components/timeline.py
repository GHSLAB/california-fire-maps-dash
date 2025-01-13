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
timeline_cn = get_timeline_item("./data/forbes/timeline_cn.json")
timeline_en = get_timeline_item("./data/forbes/timeline.json")

update_time = get_json_config("./data/forbes/update_time.json", "time")


def render():
    return [
        html.Div(
            [
                fac.AntdSpace(
                    fac.AntdFlex(
                        [
                            fac.AntdButton(
                                "翻转时间线",
                                id="switch-timeline",
                                disabled=False,
                                type="primary",
                                style=style(marginLeft="10px"),
                            ),
                            # fac.AntdButton(
                            #     fac.AntdIcon(
                            #         icon="md-translate",
                            #     ),
                            #     id="language-switch",
                            #     variant="text",
                            #     color="default",
                            #     style=style(
                            #         position="absolute", right="10px", width="32px", height="32px"
                            #     ),
                            # ),
                        ],
                    ),
                    direction="horizontal",
                    size="large",
                    style=style(marginBottom="15px"),
                ),
                html.Div(
                    [
                        fac.AntdSpace(
                            fac.AntdTimeline(
                                id="timeline", pending="持续更新中", items=timeline_cn, reverse=True
                            )
                        ),
                    ],
                    id="back-top-container-demo",
                    style={
                        "height": "calc(100vh - 300px)",
                        "maxHeight": "calc(100vh - 300px)",
                        "overflowY": "auto",
                        "position": "relative",
                        "backgroundColor": "rgba(240, 240, 240, 0.2)",
                        "borderRadius": "4px",
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
                html.Div(
                    [
                        fac.AntdText(f"更新时间：{update_time}"),
                        fac.AntdText("数据来源：福布斯", style=style(right=0)),
                    ],
                    style=style(paddingTop="10px"),
                ),
            ],
            style=style(margin="0 10px 10px 10px"),
        ),
    ]


# 回调
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


# # 回调
# @app.callback(
#     Output("timeline", "items", allow_duplicate=True),
#     Input("language-switch", "nClicks"),
#     State("timeline", "items"),
#     prevent_initial_call=True,
# )
# def switch_language(nClicks, timeline_item):
#     if nClicks and timeline_item == timeline_cn:
#         return timeline_en
#     else:
#         return timeline_cn
