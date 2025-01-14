import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_antd_charts as fact

from feffery_dash_utils.style_utils import style
from dash.dependencies import Output, Input, State

from server import app


arcgis_basemap_url = [
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}",
    # "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
]

# 转为字典
basemap = [{"url": i} for i in arcgis_basemap_url]


# 回调函数。
# 输入组件"tile-select"的"selectedUrl"属性发生变化时，触发回调函数。
# 函数作用将新选择图层URL传递给"tile-layer"，从而改变地图的底图图层。
@app.callback(Output("tile-layer", "url"), Input("tile-select", "selectedUrl"))
def change_tile_layer(selectedUrl):
    # print(selectedUrl)
    return selectedUrl
