import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

option = Options()
# 可以去掉显示的那个"自动化工具xxxx"
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 它可以取消掉webdriver
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)
web.maximize_window()
web.implicitly_wait(10)

# web = Chrome()
web.get("https://kyfw.12306.cn/otn/resources/login.html")

web.find_element(By.ID, "J-userName").send_keys("123456798")
web.find_element(By.ID, "J-password").send_keys("123456798")

web.find_element(By.ID, 'J-login').click()

time.sleep(3)
# 滑块. 怎么处理. 超级粗糙的处理
btn = web.find_element(By.ID, 'nc_1_n1z')

ac = ActionChains(web)
ac.click_and_hold(btn)  # 按住
ac.move_by_offset(xoffset=300, yoffset=0)  # 拖拽
ac.release()  # 松手
ac.perform()
time.sleep(3)

