import requests
from bs4 import BeautifulSoup


def get_forbes_timeline():

    # 目标 URL
    url = "https://www.forbes.com/sites/antoniopequenoiv/2025/01/12/california-wildfire-live-updates-death-toll-hits-24-in-palisades-eaton-fires-as-heavy-wind-expected-in-coming-days/"

    # 发送 HTTP 请求获取网页内容
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        exit()

    # 解析 HTML 内容
    soup = BeautifulSoup(response.text, "html.parser")

    # 提取所有 timeline 元素
    timeline_elements = soup.find_all("div", class_="timeline-element")

    # 整理 timeline 内容
    timeline_data = []
    for element in timeline_elements:
        # 提取时间
        time_tag = element.find("span", class_="timeline-timestamp")
        time_text = time_tag.text.strip() if time_tag else "Unknown"

        # 提取内容
        content_tag = element.find("p")
        if content_tag:
            content_text = content_tag.text.strip()
            # 如果 content_text 开头包含 time_text，则去掉开头的 time_text
            if content_text.startswith(time_text):
                content_text = content_text[len(time_text) :].strip()
        else:
            content_text = "No content"

        # 添加到结果列表
        timeline_data.append({"time": time_text, "content": content_text})

    return timeline_data
