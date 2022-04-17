import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from lxml import etree

web = Chrome()
web.implicitly_wait(10)

def get_page_source(url):
    web.get(url)
    time.sleep(3)
    return web.page_source  # selenium中的page_source 是elements

if __name__ == '__main__':
    url = "https://search.bilibili.com/all?keyword=%E5%87%A4%E5%87%B0%E8%8A%B1%E5%BC%80%E7%9A%84%E8%B7%AF%E5%8F%A3&from_source=webtop_search&spm_id_from=333.1007&page=3&o=72"
    page_source = get_page_source(url)
    tree = etree.HTML(page_source)
    txt = tree.xpath("//*[@class='video-list row']//text()")
    print(txt)