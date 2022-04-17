from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import base64
import requests
import json

def base64_api(uname, pwd, img, typeid):
    # 官方的案例. 是把一张图片. 处理成了base64
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()

    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]

web = Chrome()
web.implicitly_wait(10)  # 软等待
web.get("http://www.bilibili.com")

web.find_element(By.XPATH, '//*[@class="header-login-entry"]/span').click()

web.find_element(By.XPATH, '//*[@class="bili-mini-account"]/input').send_keys("12345789")
web.find_element(By.XPATH, '//*[@class="bili-mini-password"]/div[1]/input').send_keys("123456")

time.sleep(3)  # 这里只能硬等待
web.find_element(By.XPATH, '//*[@class="universal-btn login-btn"]').click()

tu = web.find_element(By.XPATH, '//*[@class="geetest_widget geetest_medium_fontsize"]')
tu.screenshot("tu.png")  # 把图片存储在文件中
# tu.screenshot_as_png()  # 直接拿到字节
result = base64_api("q6035945", "q6035945", "tu.png", 27)
print(result)

# 180,71|57,89|78,151
# 180,71
# 57,89
# 78,151
rs = result.split("|")
for r in rs:  # 180,71
    x, y = r.split(",")
    x = int(x)
    y = int(y)  # 转化成数字
    # 找到截图的那个位置的左上角, 横向移动xxx, 纵向移动xxx, 点击
    # 事件链, 动作链  一系列的操作
    ActionChains(web).move_to_element_with_offset(tu, xoffset=x, yoffset=y).click().perform()
    time.sleep(1)
time.sleep(1)
web.find_element(By.XPATH, "//*[@class='geetest_commit_tip']").click()
