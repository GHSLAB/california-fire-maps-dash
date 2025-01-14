class AppConfig:
    # 应用标签页title
    app_title: str = "Cal-Fire Dashboard"
    # 调试模式端口
    debug_port: int = 8000


class MapConfig:
    # 默认中心
    # california
    deafult_center: tuple = [34.198507, -118.5]
    deafult_zoom: int = 8
    # map_bounds: dict = {
    #     "minx": -119,  # 最小经度
    #     "miny": 33.5,  # 最小纬度
    #     "maxx": -118.0,  # 最大经度
    #     "maxy": 35,  # 最大纬度
    # }
