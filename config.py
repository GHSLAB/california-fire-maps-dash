class AppConfig:
    # 应用标签页title
    app_title: str = "Cal-Fire Dashboard"
    # 调试模式端口
    debug_port: int = 8000


class MapConfig:
    # 默认中心
    # california
    cal_center: tuple = [34.198507, -118.179684]
    deafult_zoom: int = 8
    cbs_bounds = [-118.702282, 34.030885, -118.013125, 34.4410175]
