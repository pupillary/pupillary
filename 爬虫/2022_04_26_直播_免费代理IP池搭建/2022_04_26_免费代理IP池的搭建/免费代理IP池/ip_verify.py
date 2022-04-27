# 这里负责代理ip的验证工作
from proxy_redis import ProxyRedis
from settings import *
import asyncio
import aiohttp
import time


# 2. 挨个的过筛子. 发送一个请求试试. 如果能正常返回. 分值拉满, 如果不OK. 扣分
# 用协程最合适

async def verify_one(ip, sem, red):
    print(f"开始检测{ip}的可用性.....")
    timeout = aiohttp.ClientTimeout(total=10)  # 10秒没回来就报错, 扣分
    async with sem:
        try:
            async with aiohttp.ClientSession() as session:  # timeout 超时时间???  10
                # requests.get(url, proxies={"http":"http://192.168.1.1:3000})
                async with session.get("http://www.baidu.com", proxy="http://"+ip, timeout=timeout) as resp:
                    page_source = await resp.text()  # str
                    if resp.status in [200, 302]:
                        # 没问题, 分值拉满
                        red.set_max_score(ip)
                        print(f"检测到{ip}, 是可用的. 分值拉满~设置成100分")
                    else:
                        # 有问题. 扣分
                        red.desc_incrby(ip)
                        print(f"检测到{ip}, 是不可用的. 抠1分")
        except Exception as e:
            print("校验IP的时候. 出错了", e)
            # 有问题. 扣分
            red.desc_incrby(ip)
            print(f"检测到{ip}, 是不可用的. 抠1分")


async def main(red):
    # 1. 把ip全都查出来
    all_proxies = red.get_all_proxy()
    sem = asyncio.Semaphore(SEM_COUNT)  # 控制并发量. 默认30
    tasks = []
    for ip in all_proxies:
        tasks.append(asyncio.create_task(verify_one(ip, sem, red)))
    if tasks:
        await asyncio.wait(tasks)


def run():
    red = ProxyRedis()
    time.sleep(START_VERIFY_WAIT_TIME)  # 初始的等待. 等待采集到数据
    while 1:
        try:
            asyncio.run(main(red))
            time.sleep(100)  # 休眠. 每隔100秒跑一次
        except Exception as e:
            print("在校验的时候. 报错了", e)
            time.sleep(100)  # 休眠. 每隔100秒跑一次


if __name__ == '__main__':
    run()
    # 进程
