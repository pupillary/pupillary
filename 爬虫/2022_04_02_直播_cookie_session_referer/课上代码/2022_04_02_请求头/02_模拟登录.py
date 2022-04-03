
# 如果我也能登录. 那么我应该也能获取到set-cookie
# 走一遍登录的流程. 应该就能拿到cookie
import requests

# 用户名, 密码, url  => 抓包

url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "16538989670",
    "password": "q6035945",
}
resp = requests.post(url, data=data)
# print(resp.headers)
# 如何拿到这一堆cookie
# print(resp.headers['Set-Cookie'])  # 字符串
# print(resp.cookies)
d = resp.cookies  # requestscookieJar

# 书架
url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp_2 = requests.get(url, cookies=d)
print(resp_2.text)

