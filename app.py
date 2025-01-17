from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output

from server import app
from config import AppConfig


import mobile


app.layout = html.Div(
    [
        fuc.FefferyDeviceDetect(id="device-detect"),
        html.Div(  # 页面渲染
            id="page-render",
            style={"margin": "10px"},
        ),
        html.Div(  # 背景图片
            style={
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "backgroundImage": "url('/assets/background.png')",
                "backgroundSize": "cover",  # 调整背景图片的大小
                "backgroundRepeat": "no-repeat",  # 防止图片重复
                "backgroundPosition": "center",  # 居中背景图片
                "opacity": "0.4",
                "zIndex": "-1",
            }
        ),
    ],
    style={"width": "100%", "height": "100vh"},
)


# 回调
# 移动端
@app.callback(Output("page-render", "children"), Input("device-detect", "deviceInfo"))
def device_detect_demo(deviceInfo):
    if deviceInfo is None or deviceInfo["isMobile"] is True:
        return mobile.render()
    else:
        return [fac.AntdCenter([fac.AntdResult(title="非移动端", subTitle="请切换为移动端访问")])]


if __name__ == "__main__":

    # app.run(port=AppConfig.debug_port, debug=True)
    app.run(host="0.0.0.0", debug=False)
