"""
输入一个网址, 浏览器会等待服务器返回东西
服务器返回东西之后。 浏览器将服务器给的东西进行展示

请求:  你向服务器发送一条消息，要东西
响应:   服务器返回给你一些消息， 返回东西
渲染:  浏览器把服务器返回的消息， 展示给用户

爬虫也要这样做
"""
# python提供了一个模块能发送请求
from urllib.request import urlopen

# 准备一个网址
url = "https://www.baidu.com"  # 就这个案例。http
resp = urlopen(url)  # 打开一个url
# print(resp)
# 从响应对象中， 提取到你需要的东西
result = resp.read()  # 从返回的东西里。拿到页面源代码
# 此时， 你会发现。打印出来的东西， 和你在浏览器看到的完全不一样
# 此时， 你打印出来的这一坨。 叫`页面源代码`
# 拿到的东西就是`页面源代码`
# print()

with open("baidu.html", mode="w", encoding="utf-8") as f:
    f.write(result.decode("utf-8"))
