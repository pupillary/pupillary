# 负责该项目中所有的关于redis的操作

# 查询
# 新增
# 增加分数
# 删除ip
# redis的连接

from redis import Redis
import random  # 随机模块

from settings import *

class ProxyRedis:
    # self.red 链接
    def __init__(self):
        self.red = Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            password=REDIS_PASSWORD,
            decode_responses=True
        )

    """
    zset
    yan{yun: 10}  # 7 
    zadd yan 20 yun
    
    需要的功能:
        1. 存储?  能直接存么?  192.168.1.1:3306  10
            先判断是否存在该IP. 如果存在. 就不进行新增操作
            
        2. 需要校验所有的ip
            查询所有ip
        3. 分值拉满 ip可用
        4. 扣分  ip不可用
        
        5. 查询可用的代理ip
            192.168.1.123 -> 90
            192.168.1.124 -> 100
            192.168.1.125 -> 100
            192.168.1.126 -> 30
            192.168.1.127 -> 5
            # 先给满分的. 
            # 没有满分的. 给有分的
            # 如果都是没有分的. 不给. 
            
    """
    def add_proxy_ip(self, ip):
        # 1.判断是否有ip
        if not self.red.zscore(REDIS_KEY, ip):
            self.red.zadd(REDIS_KEY, {ip: DEFAULT_SCORE})
            print("采集到新的IP地址了", ip)  # ??? 进库么
        else:
            print("采集到新的IP地址了", ip, "但是, 已经存在了!")  # ??? 进库么

    def get_all_proxy(self):
        return self.red.zrange(REDIS_KEY, 0, -1)

    def set_max_score(self, ip):
        self.red.zadd(REDIS_KEY, {ip: MAX_SCORE})

    def desc_incrby(self, ip):
        # 先查询出分值
        score = self.red.zscore(REDIS_KEY, ip)
        # 如果分值还有. 抠1分
        if score > MIN_SCORE:
            self.red.zincrby(REDIS_KEY, -1, ip)
        else:
            # 如果分值已经抠没了 可以再见了
            self.red.zrem(REDIS_KEY, ip)

    def get_keyong_proxy(self):
        ips = self.red.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE, 0, -1)
        if ips:
            # 随机的抽一个, 返回
            return random.choice(ips)
        else:  # 没有满分的
            ips = self.red.zrangebyscore(REDIS_KEY, DEFAULT_SCORE + 1, MAX_SCORE - 1, 0, -1)
            # 判断
            if ips:
                return random.choice(ips)
            else:
                print("实在是没有能拿得出手的ip了. ")
                return None

