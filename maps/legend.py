# legend.py
from dash import html
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style


class Legend:
    default_width = 24
    default_height = 16
    default_font_size = 14

    # 定义图例填充颜色
    @classmethod
    def fill(
        cls,
        legend_name: str,
        fill_color: str,
        box_color: str = "black",
        font_size: int = default_font_size,
        box_width: int = default_width,
        box_height: int = default_height,
    ):
        return fac.AntdSpace(
            [
                html.Div(
                    style=style(
                        width=box_width,
                        height=box_height,
                        backgroundColor=fill_color,
                        border=f"1px solid {box_color}",
                    )
                ),
                fac.AntdText(legend_name, style=style(fontSize=font_size)),
            ]
        )

    # 定义图例线段
    @classmethod
    def line(
        cls,
        legend_name: str,
        line_color: str,
        line_type: str = "solid",
        line_weight: int = 3,
        box_color: str = "black",
        box_background: str = "white",
        font_size: int = default_font_size,
        box_width: int = default_width,
        box_height: int = default_height,
    ):
        return fac.AntdSpace(
            [
                html.Div(
                    # 添加一条线段
                    html.Div(
                        style=style(
                            width=box_width,
                            height="50%",
                            borderBottom=f"{line_weight}px {line_type} {line_color}",
                        )
                    ),
                    style=style(
                        width=box_width,
                        height=box_height,
                        backgroundColor=box_background,
                        border=f"1px solid {box_color}",
                    ),
                ),
                fac.AntdText(legend_name, style=style(fontSize=font_size)),
            ]
        )
