# 先搞有界面的
# 再考虑如何没有界面
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 专门用来处理下拉框的
import time

opt = Options()
opt.add_argument("--headless")  # 无头
opt.add_argument('--disable-gpu')  # 禁用GPU
opt.add_argument("--window-size=4000,1600")  # 设置窗口大小

web = Chrome(options=opt)   # 创建浏览器
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

# 先拿数据. 然后切换年份选项
table = web.find_element(By.ID, "TableList")
print(table.text)

# 切换选项 以下内容只针对select标签
# 1.找到选择框
sel = web.find_element(By.ID, "OptionDate")  # div, span a
sel = Select(sel)

for option in sel.options:  # 拿所有的选项
    o = option.text  # 选项
    sel.select_by_visible_text(o)  # 通过文字进行选择
    #等待新的数据加载.
    time.sleep(2)
    # 先拿数据. 然后切换年份选项
    table = web.find_element(By.ID, "TableList")
    print(table.text)
