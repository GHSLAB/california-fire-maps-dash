import dash
import toml

# from config import AppConfig

# 读取 TOML 文件
with open("config.toml", "r", encoding="utf-8") as f:
    config = toml.load(f)

app = dash.Dash(__name__, title=config["app"]["title"], suppress_callback_exceptions=True)
