import json

import requests

basic_geojson = requests.get("https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json").json()

file = "./data/cbs/"

json = json.loads()
