# print("我爱你")
# print(1/0)  # 一定会报错
# print("我不爱你")
#
# while 1:
#     print("请求到百度", 1/0)  # 可能会导致某次请求不成功

"""
程序运行过程中.可能会因为各种各样的因素导致程序报错
一旦报错. 程序就会终止
需求, 程序如果报错了. 把错误交给程序来自动处理. 能不能让它别终止.

try:  # 尝试
    发送网路哦请求.......
    不出错
    得到结果了

    执行的过程中. 如果出错了
except Exception as e:
    xxxxx

try:
    活着
    吃饭,  干起来
    睡觉,  干起来
    上厕所,  干起来
except Exception as e:
    聘请律师

while 1:
    try:  # 自省
        我要发送请求到百度. 抓取百度的数据
        自己的原因出错了
        time.sleep(1)
    except Exception as e:
        print("百度报错了")

# 2 危险

"""

# try:
#     print("我爱你")
#     print(1/0)  # 1/0 =?????
#     print("我不爱你")
# except Exception as e:
#     print("出错了")
#
# print("程序不中断")

# while 1:
#     # 处理异常
#     try:  # 一般是用来处理你无法确定的问题
#         print("发请求")  # 有些情况: 一个url,不稳定
#         break
#         # print(1/0)  # 你能处理掉的问题. 一定自己处理掉.
#     except Exception as e:
#         print("  ")

# 简版.
# try:
#     pass
# except:
#     pass

# 重要的事情:
#          在学习期间.try.except. 最好是跟着樵夫的脚步去写
#          尽量的不要自己胡写.
#
#           建议, 开发阶段. 不写try..except..除非访问量非常大，url不稳定
#
import traceback
try:
    print(1/0)
except Exception as e:
    print(traceback.format_exc())  # 有需要错误调用顺序的  自取

"""
Traceback (most recent call last):
  File "D:/爬虫四期直播专用/2022_03_19_第三次直播_初识爬虫/01_异常处理.py", line 72, in <module>
    print(1/0)
ZeroDivisionError: division by zero

division by zero
"""

