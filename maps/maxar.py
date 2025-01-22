# url https://storms.ngs.noaa.gov/storms/2025_eri/index.html#11.83/34.04239/-118.46965

maxar_date_list = [
    "20250108",
    "20250109",
    "20250110",
    "20250113",
    "20250114",
    "20250116",
    "20250118",
    "20250120",
]


class MaxarServer:

    @classmethod
    def date_list(cls) -> list:
        return maxar_date_list

    @classmethod
    def url(cls, date: str) -> str:

        server_url = f"https://stormscdn.ngs.noaa.gov/{date}m-maxar/" + "{z}/{x}/{y}"

        return server_url
