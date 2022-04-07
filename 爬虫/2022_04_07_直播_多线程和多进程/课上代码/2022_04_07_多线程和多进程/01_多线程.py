
from threading import Thread  # 线程
#
# # 一个函数, 多线程多进程中表示一个任务
# def work():
#     for i in range(10000):
#         print("work中的打印", i)
#
# # 下面main 照着来. 后面讲scrapy之前, 会聊这个东西
# # 不要手敲。 m a i n  回車
# # 一个程序在被运行起来时, 会产生一个进程, 进程中会有一个默认的线程
# # 默认的进程和线程, 我们叫它, 主进程和主线程
# if __name__ == '__main__':
#     # work()  # 函数的调用. 和多线程无关
#     t = Thread(target=work)  # 创建一个线程
#     # 想要运行这个线程. 需要start()
#     t.start()  # 启动这个线程
#
#     for i in range(10000):
#         print("主线程中的打印", i)


def work(haha):
    for i in range(10000):
        print("work中的打印", haha, i)

def get_one_page_info(year):
    try:
        pass
    except Exception as e:
        pass

if __name__ == '__main__':
    # target的参数不能加括号
    # args, 参数, 必须是元组, 如果只有一个参数. 必须加逗号.
    # t1 = Thread(target=work, args=("线程1",))
    # t1.start()
    #
    # t2 = Thread(target=work, args=("线程2",))
    # t2.start()
    #
    # t3 = Thread(target=work, args=("线程3",))
    # t3.start()

    for y in range(1995, 2021):  # 200000
        get_one_page_info(y)  # ?
        t = Thread(target=get_one_page_info, args=(y, ))  # ?
        t.start()
    # 1. CPU未必扛得住.
    # 2. 创建线程也要消耗资源.
    # 3. 对方的服务器扛不住.
    # 线程数量不易太多. 一般选择CPU盒数 X 2  # 普通电脑8-16

    # 200000个任务 -> 16
    # python直接提供了线程池. 来帮助我们完成上述操作?
    # 线程池: 装有一堆线程的一个池子. 我们只需要把任务交进去就可以了.

