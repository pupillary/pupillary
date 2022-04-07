import requests
from lxml import etree
import time
from multiprocessing import Queue  # 队列
from multiprocessing import Process  # 进程
from concurrent.futures import ThreadPoolExecutor


# 图片确实在页面源代码中
# 但是, 图片不在src里, 在data-original放着
# 1.拿到页面源代码
# 2.提取data-original
# 3.下载图片

# 知识点: 进程之间是不能直接通信的(操作系统层面)

# 写一个函数. 专门负责提取data-original
# 第一个进程. 只负责提取url
def get_img_url(q):
    for page in range(1, 5):
        # 先考虑一页数据怎么抓
        url = f"https://www.pkdoutu.com/photo/list/?page={page}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        }
        resp = requests.get(url, headers=headers)
        tree = etree.HTML(resp.text)
        img_urls = tree.xpath("//li[@class='list-group-item']//img/@data-original")
        for img_url in img_urls:
            print(img_url)  # ? 7
            # 把拿到的img_url 塞入队列
            q.put(img_url)  # 固定的
    q.put("滚蛋吧.没了")   # 结束的一个消息


# 第二个进程. 只负责下载图片
def img_process(q):  # 从队列中提取url. 进行下载
    with ThreadPoolExecutor(10) as t:  # ?
        while 1:  # 这边不确定有多少个. 那就一直拿
            img_url = q.get()  # 没有问题. 这里面, get是一个阻塞的逻辑
            if img_url == '滚蛋吧.没了':
                break
            # 在进程中开启多线程(唐马儒)
            t.submit(download_img, img_url)

def download_img(url):
    # 如何下载一张图片
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    # 文件名称
    file_name = url.split("/")[-1]
    with open("./img/"+file_name, mode="wb") as f:
        f.write(resp.content)
    print("一张图片下载完成")


if __name__ == '__main__':
    # s1 = time.time()
    # get_img_url()
    # s2 = time.time()
    # print(s2-s1)

    # 准备队列
    s1 = time.time()
    q = Queue()  # 主进程 水
    p1 = Process(target=get_img_url, args=(q,))  # 单独开辟一个内存 阿大
    p2 = Process(target=img_process, args=(q,))  # 单独开辟一个内存 阿二

    p1.start()
    p2.start()

    p1.join()   # 主进程等待子进程跑完
    p2.join()   # 主进程等待子进程跑完

    s2 = time.time()
    print(s2 - s1)




