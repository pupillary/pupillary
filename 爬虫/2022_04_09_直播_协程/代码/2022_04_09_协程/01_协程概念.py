import asyncio  # python3.5?6提供的一个包

# 加上async 那么该函数就是一个协程函数
async def func():
    print("我是任务!")


if __name__ == '__main__':
    # func()  # 协程函数在加上括号之后. 产生的是一个协程对象
    # 执行协程函数的固定逻辑
    # 1.创建好协程对象.
    # 2.用asyncio包来运行该对象
    f = func()
    # 运行方案有两个
    # 1.直接run
    asyncio.run(f)  # 直接run,  windows中容易出现 "Event is Closed"
    # 2.需要获取一个事件循环的东西
    # 创建事件循环
    event_loop = asyncio.get_event_loop()
    # 运行协程对象. 直到结束
    event_loop.run_until_complete(f)  # 运行
