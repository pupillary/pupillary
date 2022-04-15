from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # 所有按键的指令
import time


web = Chrome()

web.get("https://www.zhipin.com/beijing/")

# 找到那个框框
# web.find_element_by_id()  # 过时的方案. 新版本中可能不在支持
# web.find_element_by_xpath()
# 当你使用find_xxxx如果找不到东西. 它会报错. 有可能不是下面代码的问题. 而是浏览器没有加载完成.
input_el = web.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/p/input')
input_el.send_keys("python", Keys.ENTER)  # 输入回车
time.sleep(1)
# 剩下的事情. 抓数据就完了
li_list = web.find_elements(By.XPATH, "//div[@class='job-list']/ul/li")
for li in li_list:
    # selenium用的不是一个标准的xpath语法规则
    # 最后一项不可以是@xxx, text()
    a = li.find_element(By.XPATH, ".//span[@class='job-name']/a")
    name = a.text  # 直接    节点.text
    href = a.get_property("href")  # @href
    price = li.find_element(By.XPATH, ".//span[@class='red']")
    print(name, href, price.text)

    a.click()  # 点击
    time.sleep(5)
    # 如果弹出了新窗口. 那么你需要把程序调整到新窗口里. 才能开始采集数据. 否则会报错.
    web.switch_to.window(web.window_handles[-1])  # 进入新窗口
    details = web.find_element(By.XPATH, "//div[@class='job-detail']").text
    print(details)
    print("================")
    # 关闭当前窗口
    web.close()  # 关闭了新窗口之后. selenium需要手动调整窗口到原来的窗口上
    web.switch_to.window(web.window_handles[0])

# 向框框输入内容, 敲回车
# 没有名为 selenium.web driver 的模块；selenium is not a package  。怎么办
