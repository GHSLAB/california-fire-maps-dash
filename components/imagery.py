import dash
from dash import html
import os

import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc

from feffery_dash_utils.style_utils import style


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


def satelite_compare(img1_url, img2_url):
    return html.Div(
        fuc.FefferyCompareSlider(
            firstItem=html.Img(src=img1_url, style={"width": "100%"}),
            secondItem=html.Img(src=img2_url, style={"width": "100%"}),
            style={"width": "100%"},
        ),
        style={"width": "100%"},
    )


def render():
    return [
        fac.AntdFlex(
            [
                fac.AntdTitle("数据源", level=5, className="subtitle"),
                fac.AntdSelect(),
                fac.AntdTitle("卫星影像", level=4),
                fac.AntdTitle("Eaton Fire", level=5),
                fac.AntdText("Marathon Road in Altadena, California"),
                satelite_compare("./assets/imagery/img1.webp", "./assets/imagery/img2.webp"),
                fac.AntdTitle("Palisades Fire", level=4),
                fac.AntdText("Tuna Canyon in Los Angeles"),
                satelite_compare("./assets/imagery/img3.webp", "./assets/imagery/img4.webp"),
                # fac.AntdTitle("建筑损伤", level=4),
                # fac.AntdCarousel(
                #     [
                #         fac.AntdCenter(
                #             fac.AntdImage(
                #                 src=img_url,
                #                 style={"width": "100%"},
                #             )
                #         )
                #         for img_url in damage_img_list
                #     ],
                #     arrows=True,
                #     autoplay=True,
                #     autoplaySpeed=3000,  # 500毫秒切换一次
                # ),
            ],
            vertical=True,
        )
    ]
