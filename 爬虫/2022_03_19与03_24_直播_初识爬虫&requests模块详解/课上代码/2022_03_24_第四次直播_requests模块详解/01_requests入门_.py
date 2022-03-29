import requests  # 倒进来. => 换掉urllib 发送请求

# requests的核心功能就是发送请求
# 第一个案例.

content = input("请输入一个关键字:")

url = f"https://www.sogou.com/web?query={content}"
# 发送请求
# 请求方式:get
# 你的程序现在还不够像浏览器. 人家发现了
# 装成浏览器
# 设计一个请求头.
周杰伦 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}
resp = requests.get(url, headers=周杰伦)  # 发送get请求
# requests.post()   # 发送post请求
# print(resp)  # <Response [200]>
# 获取响应体的内容(页面源代码)
# resp.read().decode()
page_source = resp.text
print(page_source)

#     响应.请求.请求头(ua)
print(resp.request.headers)

# headers = {
#     User-agent(别手写, 复制粘贴)
# }
# resp = requests.get(url, headers=?) 请求
# resp.text  => 拿到页面源代码


# 下面的逻辑要记住。看不懂的去翻录播。老师故意没写.
# Query String Parameters  => url
# key:123
# w:456
#
# Form Data    => data
# username: alex
# password: 123456
#
#
# url = "http://xxxxxxx?key=123&w=456"