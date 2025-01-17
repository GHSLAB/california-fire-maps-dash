import json
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style


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


class calFireTimeline:

    url = (
        "https://www.forbes.com/sites/antoniopequenoiv/2025/01/12/california-wildfire-live-updates-death-toll-hits-24-in-palisades-eaton-fires-as-heavy-wind-expected-in-coming-days/",
    )

    @classmethod
    def update_time(cls):
        return get_json_config("./data/forbes/update_time.json", "Last updated")

    @classmethod
    def translate_time(cls):
        return get_json_config("./data/forbes/translate_time.json", "Last updated")

    @classmethod
    def items(cls):
        return get_timeline_item("./data/forbes/timeline.json")

    @classmethod
    def items_cn(cls):
        return get_timeline_item("./data/forbes/timeline_cn.json")
