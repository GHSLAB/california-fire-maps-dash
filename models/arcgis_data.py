import requests
from urllib.parse import urlparse
from datetime import datetime
import os
import shutil

url_lists = {
    "arcgis": [
        "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/aircraft/aircraftfeed-gj.json",
        "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/incidents/incidents-gj.json",
        "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/cameras/alertCACameras-gj.json",
        "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/weather/wind-raws-gj.json",
        "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/evacuations/evacuations-gj.json",
    ]
}


class ArcGISData:

    url_lists = {
        "arcgis": [
            "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/aircraft/aircraftfeed-gj.json",
            "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/incidents/incidents-gj.json",
            "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/cameras/alertCACameras-gj.json",
            "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/weather/wind-raws-gj.json",
            "https://rdipowerplatformfd-e5hhgqaahef7fbdr.a02.azurefd.net/evacuations/evacuations-gj.json",
        ]
    }

    @classmethod
    def get_data(cls, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
