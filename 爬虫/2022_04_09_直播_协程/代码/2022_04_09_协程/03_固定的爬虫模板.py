import asyncio
import time


async def get_page_source(url):
    # 网络请求, requests 不支持异步
    print("发请求到", url)
    await asyncio.sleep(3)  # ????
    print("拿到了页面源代码")
    return " 我就是源代码. 你敢用么?? "


async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.taobao.com",
        "http://www.google.com",
    ]
    tasks = []
    for url in urls:
        f = get_page_source(url)
        t = asyncio.create_task(f)  # 这里其实就已经开始启动了. 但是执行完了么?
        tasks.append(t)
    await asyncio.wait(tasks)
    # 如果需要返回值
    # 方案一.
    # jay, pending = await asyncio.wait(tasks)  # 拉出去~~~~
    # for r in jay:
    #     print(r.result())  # 拿结果    result() 定死的

    # 方案二.
    # results = await asyncio.gather(*tasks)  # 和wait功能差不多   去翻python基础.
    # for r in results:
    #     print(r)

if __name__ == '__main__':
    s1 = time.time()
    asyncio.run(main())
    s2 = time.time()
    print(s2 - s1)


