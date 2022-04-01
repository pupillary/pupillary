import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


url = "https://desk.zol.com.cn/pc/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
resp = requests.get(url, headers=headers)
resp.encoding = "gbk"
# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
# main_page.find(标签, attrs={})
# main_page.find_all(标签, attrs={})
# main_page.select_one(css选择器)  # 选一个
# main_page.select(css选择器)  # 选一堆

# 根本目标: 拿到每个详情页的url地址 => a
a_list = main_page.select(".photo-list-padding > a")
for a in a_list:
    href = a.get("href")

    if href.endswith("exe"):
        continue
    href = urljoin(url, href)
    print(href)

    child_resp = requests.get(href, headers=headers)
    child_resp.encoding = "gbk"
    child_page = BeautifulSoup(child_resp.text, "html.parser")
    # re => 拿json => loads  => 解析  => 真正的图片地址 => 下载(9张)
    src = child_page.select_one("#bigImg").get("src")

    img_resp = requests.get(src, headers=headers)
    file_name = src.split("/")[-1]
    with open(file_name, mode="wb") as f:
        f.write(img_resp.content)
    print("一张图完事儿")
    time.sleep(1)
