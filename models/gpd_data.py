import geopandas as gpd
import pandas as pd
import os
import datetime

import json


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)


def calculate_time_difference(time_str):
    """
    计算起火时间至当前时间（UTC）的时间差，并格式化为字符串。

    :param time_str: 起火时间字符串，格式为'YYYY-MM-DD HH:MM:SS+00:00'
    :return: 格式化后的时间差字符串，格式为'X天X小时X分钟'
    """
    # 将时间字符串转换为datetime对象
    time_obj = datetime.datetime.fromisoformat(time_str)
    # 获取当前时间（UTC）
    current_time = datetime.datetime.now(tz=datetime.timezone.utc)
    # 计算时间差
    time_difference = current_time - time_obj
    # 提取天数、小时数和分钟数
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    # 格式化时间差为字符串
    formatted_time_difference = f"{days}天{hours}小时{minutes}分钟"
    return formatted_time_difference


def get_geojson_creation_time(file_path):
    """
    获取GeoJSON文件的创建时间。

    :param file_path: GeoJSON文件的路径
    :return: 文件的创建时间，格式为字符串
    """
    # 获取文件的创建时间戳
    creation_time_timestamp = os.path.getctime(file_path)

    # 将时间戳转换为datetime对象
    creation_time_datetime = datetime.fromtimestamp(creation_time_timestamp)

    # 将datetime对象格式化为字符串
    creation_time_string = creation_time_datetime.strftime("%Y-%m-%d %H:%M:%S")

    return creation_time_string


class cbsdata:

    gdf_cbs_fire = gpd.GeoDataFrame.from_features(
        read_json_file("./data/latest/cbs/latest_cali_fires.geojson")
    )
    gdf_cbs_evac = gpd.GeoDataFrame.from_features(
        read_json_file("./data/latest/cbs/latest_cali_evac.geojson")
    )

    update_time = gdf_cbs_evac["timestamp"].max()

    @classmethod
    def evac_gdf(cls):
        return cls.gdf_cbs_evac

    @classmethod
    def evac_gdf_to_json(cls):
        """
        这个错误提示表明在将数据转换为JSON格式时，遇到了一个Timestamp类型的对象，
        而JSON无法直接序列化这个对象。Timestamp是Pandas库中用于表示时间戳的数据类型。

        要解决这个问题，你需要在将数据转换为JSON之前，将Timestamp对象转换为字符串或其他可序列化的格式。
        你可以通过在to_json方法中指定date_format参数来实现这一点。
        """
        # 使用json.loads()将gdf.to_json字符串转换为JSON格式
        return json.loads(cls.gdf_cbs_evac.to_json())

    @classmethod
    def evac_timestamp(cls):
        return cls.update_time

    @classmethod
    def evac_order_gdf(cls):
        return cls.gdf_cbs_evac[cls.gdf_cbs_evac["status"] == "Evacuation Order"]

    @classmethod
    def evac_warning_gdf(cls):
        return cls.gdf_cbs_evac[cls.gdf_cbs_evac["status"] == "Evacuation Warning"]

    @classmethod
    def evac_order_gdf_to_json(cls):
        # 使用json.loads()将gdf.to_json字符串转换为JSON格式
        json_data = cls.gdf_cbs_evac[cls.gdf_cbs_evac["status"] == "Evacuation Order"]
        return json.loads(json_data.to_json())

    @classmethod
    def evac_warning_gdf_to_json(cls):
        # 使用json.loads()将gdf.to_json字符串转换为JSON格式
        json_data = cls.gdf_cbs_evac[cls.gdf_cbs_evac["status"] == "Evacuation Warning"]
        return json.loads(json_data.to_json())

    @classmethod
    def fire_gdf(cls):
        return cls.gdf_cbs_fire

    @classmethod
    def fire_gdf_to_json(cls):
        # 使用json.loads()将gdf.to_json字符串转换为JSON格式
        return json.loads(cls.gdf_cbs_fire.to_json())

    @classmethod
    def burn_area_dict(cls):
        cls.gdf_cbs_fire["烧毁面积(km2)"] = round(cls.gdf_cbs_fire["acres_burned"] * 0.00404686, 2)
        return (
            cls.gdf_cbs_fire[["fire_name", "烧毁面积(km2)"]]
            .sort_values(by="烧毁面积(km2)", ascending=False)
            .to_dict("records")
        )


###
class arcgisdata:
    incidents = gpd.GeoDataFrame.from_features(
        read_json_file("./data/latest/arcgis/incidents-gj.json")
    )
    wind = gpd.GeoDataFrame.from_features(read_json_file("./data/latest/arcgis/wind-raws-gj.json"))

    aircraft = gpd.GeoDataFrame.from_features(
        read_json_file("./data/latest/arcgis/aircraftfeed-gj.json")
    )

    # display_df = active_fire[
    #     [
    #         "name",
    #         "started",
    #         "acresBurned",
    #         "percentContained",
    #         "structuresDestroyed",
    #         "structuresDamaged",
    #         "structuresThreatened",
    #     ]
    # ]

    @classmethod
    def incidents_count(cls):
        return cls.active_fire.count()

    # 当前进度
    @classmethod
    def save_progress_dict(cls, type: str):
        active_fire = cls.incidents[cls.incidents["status"] == "Active"]
        save_df = active_fire[["name", "started", "acresBurned", "percentContained"]]

        # 将 "起火时间" 字段的内容转换为分钟精度
        save_df["起火时间"] = pd.to_datetime(save_df["started"]).dt.strftime("%m-%d %H:%M")

        # # 计算当前UTC时间至started字段时间的时间差
        # save_df["火情时间"] = pd.to_datetime(save_df["started"]).apply(
        #     lambda x: datetime.datetime.now(tz=datetime.timezone.utc) - x
        # )
        save_df["烧毁面积"] = round(save_df["acresBurned"] * 0.00404686, 2)
        # 将 "火势控制进度" 字段的内容转换为百分比格式
        save_df["火势控制进度"] = save_df["percentContained"].astype(float) / 100

        save_df = save_df.dropna()
        if type == "charts":
            return save_df.sort_values(by="火势控制进度", ascending=False).to_dict("records")

        elif type == "columns":
            columns_dict = [
                ({"title": f"{column}", "dataIndex": f"{column}"})
                for column in save_df.columns.to_list()
            ]
            # print(columns_dict)
            return columns_dict

        elif type == "data":
            return save_df.sort_values(by="火势控制进度", ascending=False).to_dict("records")
        else:
            return None

    @classmethod
    def save_resoucres_dict(cls):
        active_fire = cls.incidents[cls.incidents["status"] == "Active"]
        save_df = active_fire[["name", "helicopters", "engines", "dozers", "waterTenders"]]
        save_df = save_df.dropna()
        save_list = []
        for index, row in save_df.iterrows():
            save_list.append({"名称": row["name"], "类型": "直升机", "数量": row["helicopters"]})
            save_list.append({"名称": row["name"], "类型": "消防车", "数量": row["engines"]})
            save_list.append({"名称": row["name"], "类型": "推土机", "数量": row["dozers"]})
            save_list.append({"名称": row["name"], "类型": "水罐车", "数量": row["waterTenders"]})
        return save_list

    @classmethod
    def casualties_dict(cls):
        active_fire = cls.incidents[cls.incidents["status"] == "Active"]
        save_df = active_fire[
            [
                "name",
                "civilianInjuries",
                "civilianFatalities",
                "firefighterInjuries",
                "firefighterFatalities",
            ]
        ]
        # 首先，检查'column_name'列中哪些行是NaN（空值）
        nan_rows = save_df["civilianFatalities"].isnull()

        # 然后，使用~操作符来选择非空的行
        non_save_df = save_df[~nan_rows]

        # save_df = save_df.dropna()
        save_list = []
        for index, row in non_save_df.iterrows():
            save_list.append(
                {"名称": row["name"], "类型": "平民受伤", "数量": row["civilianInjuries"]}
            )
            save_list.append(
                {"名称": row["name"], "类型": "平民死亡", "数量": row["civilianFatalities"]}
            )
            save_list.append(
                {"名称": row["name"], "类型": "消防员受伤", "数量": row["firefighterInjuries"]}
            )
            save_list.append(
                {"名称": row["name"], "类型": "消防员死亡", "数量": row["firefighterFatalities"]}
            )
        return save_list
