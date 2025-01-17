from dash import html

import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style


duzhe1 = """　　后来，我到美国的黄石公园游览。一些笔自的松树歪歪斜斜倒在林子里无人过问，这么好的木材是完全可以利用的，白白放在这里腐烂岂不可惜?导游告诉我，这里的树木只能烂在林子里，谁也没有权利将它们作为他用。导游还向我说了一个更为惊人的事情，他说夏季的电闪雷鸣往往会引起黄石公园森林大火，但你也许会在路上看到一个大牌子，上面写着："森林正在着火，请不要报警。"这让我感到不可思议，但仔细想，这正符合自然状态下生与灭的自然法则啊。被焚烧过的森林，在为新的更茂盛的森林创造出空间和更加肥沃的土壤。"""
duzhe2 = """　　经历了这些以后，也许我可以向儿子解释什么是生态平衡了：按照自然规律去尊重自然，尊重自然所固有的生存、灭亡和发展的秩序与规则。"""


def render():
    return [
        fac.AntdCenter(
            fac.AntdFlex(
                [
                    fac.AntdTitle("本应用仅为技术测试", level=5),
                    fac.AntdText("数据定时抓取, 非实时消息, 仅供参考"),
                    fac.AntdDivider(style=style(marginTop="5px", marginBottom="5px")),
                    fac.AntdTitle("欢迎关注公众号交流", level=5),
                    fac.AntdImage(
                        src="/assets/qrcode.png",
                        style=style(width="250px"),
                    ),
                    fac.AntdDivider(),
                    fac.AntdText("项目地址:"),
                    html.A(
                        "Github-GHSLAB/california-fire-maps-dash",
                        href="https://github.com/GHSLAB/california-fire-maps-dash",
                    ),
                    fac.AntdTitle("Power by:", level=5),
                    fac.AntdText("Python - Dash"),
                    fac.AntdText("feffery-antd-components"),
                    fac.AntdText("feffery-antd-charts"),
                    fac.AntdText("feffery-leaflet-components"),
                    fac.AntdText("feffery_utils_components"),
                    fac.AntdTitle("Data Source:", level=5),
                    html.A(
                        "github cbs-news-data",
                        href="https://cbs-news-data.github.io/socal-fire-evacs_maplibre/",
                    ),
                    html.A(
                        "Southern California Fires January 2025",
                        href="https://calfire-forestry.maps.arcgis.com/home/item.html?id=0a7381c8b46b4e26a057383424f32c06",
                    ),
                    html.A(
                        "https://www.fire.ca.gov",
                        href="https://www.fire.ca.gov",
                    ),
                    html.A(
                        "https://hub.wftiic.ca.gov",
                        href="https://hub.wftiic.ca.gov",
                    ),
                    html.A(
                        "https://protect.genasys.com/hazards",
                        href="https://protect.genasys.com/hazards",
                    ),
                    html.A(
                        "https://storms.ngs.noaa.gov",
                        href="https://storms.ngs.noaa.gov/storms/2025_eri/index.html",
                    ),
                ],
                vertical=True,
            )
        ),
        # fac.AntdDivider(
        #     style=style(marginBottom="10px"),
        # ),
        fac.AntdFlex(
            [
                html.A(
                    "闽ICP备2023008814号-3",
                    href="https://beian.miit.gov.cn/",
                    style=style(fontSize="12px", color="#8B8B8B"),
                ),
            ],
            justify="space-around",
            align="flex-end",
            style=style(width="100%", position="fixed", bottom="10px"),
        ),
    ]
