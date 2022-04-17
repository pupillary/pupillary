# 用requests来完成登录过程
# 一般情况下. 在使用验证码的时候. 要保持住会话. 否则容易引起,验证码识别不成功的现象
import time

import requests
import base64
import json


def base64_api(uname, pwd, img, typeid):
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}  # 直接把img搞进来
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


session = requests.session()
# 1.设置好头信息
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}

# 2. 加载一个最原始的cookie(可能需要可能不需要. 好习惯)
session.get("http://www.ttshitu.com/login.html?spm=null")

# 3. 发送请求. 拿到验证码
verify_url = "http://admin.ttshitu.com/captcha_v2?_=1650111626736"  # url屁股上总能看见_ t n  => 时间戳
resp = session.get(verify_url)
img = resp.json()['img']  # 拿图片
imgId = resp.json()['imgId']  # 图片ID

# 4.识别验证码
verify_code = base64_api("q6035945", "q6035945", img, 1)

username = "q6035945"
password = "q6035945"

# 准备登录
login_url = "http://admin.ttshitu.com/common/api/login/user"
data = {
    "captcha": verify_code,
    "developerFlag": False,
    "imgId": imgId,
    "needCheck": True,
    "password": password,
    "userName": username,
}
# 我们在浏览器中发现了一种全新的参数逻辑
# Request Payload
# 第一, 发送出去的是json
# 第二, 请求一定是post
# 第三, 它的请求头里一定有content-type:application/json;
# resp = session.post(login_url, data=json.dumps(data), headers={"Content-Type": "application/json; charset=UTF-8"})
resp = session.post(login_url, json=data)  # 如果给了json参数. 自动的帮你转化和处理. 以及请求头的处理
print(resp.text)
