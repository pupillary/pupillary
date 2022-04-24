import redis

red = redis.Redis(
    host="127.0.0.1",
    port=6379,
    password="123456",
    db=3,
    decode_responses=True  # 不写它. 中文是乱码
)
# #   命令 key 值
# red.set("alex", "大傻蛋")
#
# red.save()

# r = red.get("alex")
# print(r)

# red.hset("wusir", "name", "武沛齐")
# red.hset("wusir", "age", 18)
# red.save()

# r = red.hmget("wusir", "name", "age")
# print(r)
#
# r = red.hgetall("wusir")
# print(r)

# red.lpush("stu", "九曲", "cool", "昆磨")
# r = red.lrange("stu", 0, -1)
# print(r)

# red.sadd("teachers", "听雨", "燕归来", "蔡徐坤")

# r = red.smembers("teachers")
# print(r)

# zset 这玩意有点儿坑


# zadd dakey xxxx 101 xxxx 20 xxxx 30
# red.zadd("yan", {"cool": 10, "kunmo":20, "zhangjiafeng": 5})

# r = red.zrange("yan", 0, -1)
# print(r)

# r = red.zrange("yan", 0, -1, withscores=True)
# print(r)

# 如果要存储列表或者字典或者列表套字典. 或者字典套列表

lst = ["张国强", "宋福贵", "徐长江"]
# 1. 直接用set存
import json
# red.set("names", json.dumps(lst))
s = red.get("names")
lst = json.loads(s)
print(lst)
red.close()  # 断开连接
