import requests
from bs4 import BeautifulSoup  # 导入BeautifulSoup
from urllib.parse import urljoin  # 专门用来做url路径拼接的
import time

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}
url = "https://desk.zol.com.cn/pc/"
resp = requests.get(url, headers=header)
resp.encoding = "gbk"  # 设置编码
main_page_source = resp.text
print(type(main_page_source))

# 需要解析页面源代码. 获取到a标签中的href的值
# 直接把页面源代码塞进去

main_page = BeautifulSoup(main_page_source, "html.parser")

# 从BeautifulSoup  提取你要的东西
a_list = main_page.find("ul", attrs={"class": "pic-list2"}).find_all("a")
for a in a_list:
    # 我需要的是a标签的href
    # 想要从bs4里面拿到某一个标签的某一个属性
    href = a.get("href")  # get(属性)
    if href.endswith(".exe"):  # 判断字符串href是否以.exe结尾
        continue

    text = a.find("em").text  # 文本

    # 你的href是不完整的, 是需要拼接的
    # 用你获取到这个href的url和href拼接
    # 必须记住. 好用
    href = urljoin(url, href)

    # 我要访问详情页. 获取图片下载地址
    child_resp = requests.get(href, headers=header)
    child_resp.encoding = "gbk"
    child_page_source = child_resp.text

    child_page = BeautifulSoup(child_page_source, "html.parser")
    # 可能会有风险, NoneType xxxx
    src = child_page.find("img", attrs={"id": "bigImg"}).get("src")
    print(src)

    # 下载图片
    img_resp = requests.get(src)
    # 1. 如果a中的名字不重复, 可以用a的文字
    # 2. 如果a中的名字重复,  可以使用路径中的名字
    file_name = src.split("/")[-1]
    with open(file_name, mode="wb") as f:
        f.write(img_resp.content)
    # break   # 测试用
    time.sleep(1)
