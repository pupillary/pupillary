import requests
from lxml import etree

# 1.拿页面源代码#
# 2.xpath提取数据

# //table/tbody/tr
url = "http://www.boxofficecn.com/boxoffice2022"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.text)
page = etree.HTML(resp.text)
trs = page.xpath("//table/tbody/tr")[1:-1]
# tr全是数据
for tr in trs:
    num = tr.xpath("./td[1]/text()")
    year = tr.xpath("./td[2]//text()")
    name = tr.xpath("./td[3]//text()")[0]

    # py基础
    if name:
        "".join(name)  # 这是合理的方案
    money = tr.xpath("./td[4]/text()")

    print(num, year, name, money)



# 不正常
movie1 = ['京北的我们（', '重映', '）']  # 京北的我们（重映）
len(movie1)  # ???? 3

# 正常的  1
movie2 = ['不要忘记我爱你']
# 这个是空
movie3 = []
