import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

def get_proxy():
    url = "http://127.0.0.1:5800/get_proxy"
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    dic = resp.json()
    proxy = {
        "http": "http://" + dic["ip"],  # http可用
        "https": "http://" + dic["ip"],  # https不可用
    }
    print(proxy)
    return proxy


url = "http://www.baidu.com/s?wd=ip"
# 上述url会自动的重定向到https上
# requests 会自动的像浏览器一样帮助我们完成这个重定向
# 第一次请求的是http. 被重定向了.
# 第二次请求的是https
resp = requests.get(url, proxies=get_proxy(), headers=headers)
print(resp.text)  # 检测 <script type="text/javascript" data-compress="off">
