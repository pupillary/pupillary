import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}

# 准备代理
dic = {
    "http": "http://223.96.90.216:8085",
    "https": "https://223.96.90.216:8085",
}
# proxies = 代理
resp = requests.get("http://www.baidu.com/s?ie=UTF-8&wd=ip", proxies=dic, headers=headers)

print(resp.text)
