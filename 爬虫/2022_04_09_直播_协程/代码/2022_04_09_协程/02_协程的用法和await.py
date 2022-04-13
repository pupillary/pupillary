import asyncio
import time

# 创建协程函数
async def func1():
    print("我是func1要开始了")
    # 模拟
    # time.sleep(5)  # 这里不能用time.sleep() 因为sleep不支持协程
    # await 挂起, 等, 等着任务结束. 回到这里继续执行
    # 被挂起的时候. cpu切换到其他任务身上了
    await asyncio.sleep(3)
    print("我是func1结束了")


async def func2():
    print("我是func2要开始了")
    await asyncio.sleep(5)
    print("我是func2结束了")


async def func3():
    print("我是func3要开始了")
    await asyncio.sleep(2)
    print("我是func3结束了")


async def main():
    # 创建三个协程对象
    f1 = func1()  # 苹果
    f2 = func2()
    f3 = func3()
    # 把三个协程对象都封装成任务对象
    t1 = asyncio.create_task(f1)  # 盒装苹果
    t2 = asyncio.ensure_future(f2)
    t3 = asyncio.create_task(f3)

    # 等待三个任务结束
    tasks = [t1, t2, t3]
    # await 叫挂起 => 拉出来. 放外面去等着
    # 挂起, 边上带着, 等着完事儿了. 再回来
    await asyncio.wait(tasks)  # 市场
    print(123456)


if __name__ == '__main__':
    s1 = time.time()
    # event = asyncio.get_event_loop()
    # event.run_until_complete(main())
    asyncio.run(main())
    s2 = time.time()
    print(s2 - s1)
