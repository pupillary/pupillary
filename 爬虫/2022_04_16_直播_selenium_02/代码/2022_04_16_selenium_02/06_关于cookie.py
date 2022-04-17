from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

url = "https://www.17k.com/"

web = Chrome()
web.implicitly_wait(5)
web.get(url)
web.maximize_window()

# 进入登录
web.find_element(By.XPATH, '//*[@id="header_login_user"]/a[1]').click()

iframe = web.find_element(By.XPATH, "/html/body/div[20]/div/div[1]/iframe")
web.switch_to.frame(iframe)

time.sleep(1)
# 输入用户名密码
web.find_element(By.XPATH, '/html/body/form/dl/dd[2]/input').send_keys("16538989670")
web.find_element(By.XPATH, '/html/body/form/dl/dd[3]/input').send_keys("q6035945")
# 协议
web.find_element(By.XPATH, '//*[@id="protocol"]').click()  # 协议
# 登录
web.find_element(By.XPATH, '/html/body/form/dl/dd[5]/input').click()

# 登录成功之后. 睡眠一下下.
time.sleep(1)
# 记录cookie
cookies = web.get_cookies()  # 加载的cookie是浏览器上的cookie 所以, 包括了服务器返回的cookie和js执行加载的cookie

# 假设cookie准备给requests使用的话.
cookie = {}
for item in cookies:
    name = item['name']
    value = item['value']
    cookie[name] = value

# 后面的requests就可以直接使用cookie了
import requests

resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", cookies=cookie)
print(resp.text)


