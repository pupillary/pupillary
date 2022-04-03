import requests

# 1.创建一个session
session = requests.session()

# 2.可以提前给session设置好请求头或者cookie
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}

# 可用, 可不用
# session.cookies = {
#     # 可以把一些cookie的内容塞进来, 这里要的是字典
# }

# 3. 发请求

# 登录
url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "16538989670",
    "password": "q6035945",
}
# requests.post(url, data=data)
session.post(url, data=data)  # resp.header set-cookie
# javascript不管

# 后续的所有请求. 都会带着cookie
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp_2 = session.get(url)
# print(resp_2.text)

# 保持会话 -> session
