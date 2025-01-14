class AppConfig:
    # 应用标签页title
    app_title: str = "Cal-Fire Dashboard"
    # 调试模式端口
    debug_port: int = 8000


class MapConfig:
    # 天地图地址
    tianditu_url: str = "http://127.0.0.1/server/tiles/tianditu/{z}/{x}/{y}.png"
    tianditu_cia_url: str = "http://127.0.0.1/server/tiles/tianditu_cia/{z}/{x}/{y}.png"

    arcgis_imagery: str = (
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    )
    labels: str = "https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}{r}.png"

    # 默认中心
    # california
    cal_center: tuple = [34.198507, -118.139684]
    deafult_center: dict = {"lat": 24, "lng": 118}
    deafult_zoom: int = 8
