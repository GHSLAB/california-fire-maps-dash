import re
import pandas as pd


class access_log:

    log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/1.\d" (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'

    # 读取日志文件
    log_file = "./logs/access.log"

    @classmethod
    def method_counts(cls):
        logs = []

        with open(cls.log_file, "r") as f:
            for line in f:
                match = re.match(cls.log_pattern, line)
                if match:
                    logs.append(match.groupdict())

        # 将日志转换为 DataFrame
        df = pd.DataFrame(logs)

        # 统计每个方法的数量
        method_counts = df["method"].count()
        return method_counts
