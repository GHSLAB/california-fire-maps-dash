import dash
from dash import html
import os

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output

from server import app


# damage image
def get_all_files_list(directory: str) -> list:
    """
    获取指定文件夹路径中的所有文件，并返回相对路径的列表

    参数:
    directory (str): 指定的文件夹路径

    返回:
    list: 包含文件夹中所有文件相对路径的列表
    """
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, directory)
            files.append(directory + relative_path)
    return files


# 获取文件夹中的所有文件的相对路径
damage_img_list = get_all_files_list("./assets/news/damage/")
# print(damage_img_list)


def damage_img():
    return fac.AntdCarousel(
        [
            fac.AntdCenter(
                fac.AntdImage(
                    src=img_url,
                    style={"width": "100%"},
                )
            )
            for img_url in damage_img_list
        ],
        arrows=True,
        autoplay=True,
        autoplaySpeed=3000,  # 500毫秒切换一次
    )


def satelite_compare(img1_url, img2_url):
    return html.Div(
        fuc.FefferyCompareSlider(
            firstItem=html.Img(src=img1_url, style={"width": "100%"}),
            secondItem=html.Img(src=img2_url, style={"width": "100%"}),
            style={"width": "100%"},
        ),
        style={"width": "100%"},
    )


def palisades_img():
    return [
        fac.AntdTitle("Palisades Fire", level=5, style=style(marginTop="5px")),
        fac.AntdText("2025-1-6 vs 1-8"),
        satelite_compare("./assets/imagery/palisades-1.webp", "./assets/imagery/palisades-2.webp"),
        satelite_compare("./assets/imagery/img5.webp", "./assets/imagery/img6.webp"),
        fac.AntdText("Tuna Canyon in Los Angeles"),
        satelite_compare("./assets/imagery/img3.webp", "./assets/imagery/img4.webp"),
    ]


def eaton_img():
    return [
        fac.AntdFlex(
            [
                fac.AntdTitle("Eaton Fire", level=5, style=style(marginTop="5px")),
                fac.AntdImage(
                    src="./assets/rs/maxar.webp",
                    style={"width": "100%"},
                ),
                fac.AntdText("2025-1-6 vs 1-8 Marathon Road in Altadena, California"),
                fac.AntdText("加利福尼亚州阿尔塔迪纳住宅区"),
                satelite_compare("./assets/imagery/img1.webp", "./assets/imagery/img2.webp"),
            ],
            vertical=True,
        )
    ]


def render():
    return [
        fac.AntdFlex(
            [
                fac.AntdTitle("新闻影像", level=4, style=style(marginTop="5px")),
                fac.AntdSelect(
                    id="location-select",
                    options=[
                        {"label": "Palisades 地区", "value": "Palisades"},
                        {"label": "Eaton 地区", "value": "Eaton"},
                        {"label": "损毁建筑", "value": "damage"},
                    ],
                ),
                html.Div(
                    id="imagery-container",
                    style={"width": "100%", "padding": "5px", "marginTop": "5px"},
                ),
            ],
            vertical=True,
        )
    ]


@app.callback(Output("imagery-container", "children"), Input("location-select", "value"))
def update_imagery(location):
    if location == "Eaton":
        return eaton_img()
    elif location == "Palisades":
        return palisades_img()
    elif location == "damage":
        return damage_img()
    else:
        return []
