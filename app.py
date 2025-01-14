import dash
from dash import dcc
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output

from server import app
from config import AppConfig, MapConfig


import mobile


app.layout = html.Div(
    [
        fuc.FefferyDeviceDetect(id="device-detect"),
        html.Div(
            id="page-render",
            style={"margin": "15px"},
        ),
    ],
    style=style(width="100%"),
)


# 回调
# 移动端
@app.callback(Output("page-render", "children"), Input("device-detect", "deviceInfo"))
def device_detect_demo(deviceInfo):
    if deviceInfo["isMobile"] is True:
        return mobile.render()
    else:
        return [fac.AntdCenter([fac.AntdResult(title="非移动端", subTitle="请切换为移动端访问")])]


if __name__ == "__main__":
    app.run(port=AppConfig.debug_port, debug=True)
    # app.run(host="0.0.0.0", debug=False)
