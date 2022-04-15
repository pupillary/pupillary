# 1. selenium的包都很长
# 导入驱动的py包
from selenium.webdriver import Chrome

web = Chrome()
# 打开url
web.get("https://www.baidu.com/")

web.maximize_window()  # 设置为最大窗口

# 拿到一些内容
print(web.title)
