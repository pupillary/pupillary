import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time


def str_tools(lst):
    if lst:
        s = "".join(lst)
        return s.strip()
    else:
        return ""


def get_movie_info(year):
    # 抓取1996年的电影票房
    f = open(f"{year}.csv", mode="w", encoding="utf-8")
    url = f"http://www.boxofficecn.com/boxoffice{year}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//table/tbody/tr")[1:]
    for tr in trs:
        num = tr.xpath("./td[1]//text()")
        year = tr.xpath("./td[2]//text()")
        name = tr.xpath("./td[3]//text()")
        money = tr.xpath("./td[4]//text()")

        num = str_tools(num)  # ???
        year = str_tools(year)  # ???
        name = str_tools(name)  # ???
        money = str_tools(money)  # ???

        f.write(f"{num},{year},{name},{money}\n")


if __name__ == '__main__':
    # s1 = time.time()  # 当前系统时间的时间戳
    # for y in range(1994, 2023):
    #     get_movie_info(y)
    # s2 = time.time()  # 执行之后的时间戳
    # print(s2 - s1)  # 16.23

    # 效果不够好. 有丢失数据现象.这个网站不能直接这么干. 需要数据的验证或者单线程.
    s1 = time.time()
    with ThreadPoolExecutor(20) as t:
        for y in range(1994, 2023):
            t.submit(get_movie_info, y)  # 交任务
    s2 = time.time()
    print(s2 - s1)  # 如果用来下载图片. 视频等资源. 效果会比这个好n倍

