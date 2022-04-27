import test1  # 这里如果有红线. 不用管

# python中. 所有的xxxx.py文件实际上是 xxxx模块
# 当你import xxx的时候. 它会自动的把xxx.py文件给运行了
# 那么这里会产生一个问题. test1中的变量会去哪里
# 会不会产生冲突

# 在导入模块时, 系统会自动的给这个模块开辟一块内存空间
# 在该内存空间中执行该py文件
# 这个空间就是你导入的这个模块

# name = "wusir"
#
# print(name)
# print(test1.name)

# import test1
# test1.get()

# from test1 import get
# 在导入模块时, 系统会自动的给这个模块开辟一块内存空间
# 在该内存空间中执行该py文件
# 这个空间就是你导入的这个模块

# import time

# import test1
# import test1
# import test1
# import test1
# import test1
# import test1
# import test1
# import test1
# import test1
# import test1
# from test1 import get
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#


# if __name__ == '__main__':

