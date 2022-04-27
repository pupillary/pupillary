

name = "alex"
#
def get():
    print("我是get")


# 我在写程序的时候留下的一个测试代码
# 下面的代码是不希望别人在import的时候就运行的.
# get()  # 直接把程序执行了
# print(__name__)  # python的每一个py文件默认都有一个变量
# __main__ : 右键运行该py文件的时候
# test1 : 在该py文件被import的时候

# 你要把当前py文件作为启动文件的时候才会执行
# 当你的py文件被import的时候. 下面的代码就不执行了.
if __name__ == '__main__':  # 我是自己右键运行的时候
    get()
