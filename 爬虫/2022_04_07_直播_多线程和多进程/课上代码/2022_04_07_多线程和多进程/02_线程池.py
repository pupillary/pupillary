from concurrent.futures import ThreadPoolExecutor

def work(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # # 1.先造线程池
    # with ThreadPoolExecutor(16) as t:
    #     # 提交
    #     # t.submit(任务, 任务执行时需要的参数)
    #     # Thread(target=任务, args=(任务执行时需要的参数,)
    #     t.submit(work, "线程1")
    #     t.submit(work, "线程2")
    #     t.submit(work, "线程3")
    #     t.submit(work, "线程4")
    #     pass
    # # 以后用线程池. 直接写with
    # # 结束之后. 自动完成一些操作

    # 4个任务. 你希望四个任务一期跑
    # A
    with ThreadPoolExecutor(16) as t:
        for i in range(4):
            t.submit(work, f"线程{i}")

    # B   性能很像单线程. 机器性能差一些. 不如单线程?
    for i in range(4):
        with ThreadPoolExecutor(16) as t:
            t.submit(work, f"线程{i}")
