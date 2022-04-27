
# redis主机ip地址
REDIS_HOST = "127.0.0.1"
# redis端口号
REDIS_PORT = 6379
# redis的数据库
REDIS_DB = 5
# redis密码
REDIS_PASSWORD = "123456"

# 存储在redis中的代理ip的key. 建议不更换
REDIS_KEY = "proxy_ip"

# 默认的ip分值
DEFAULT_SCORE = 10
# 满分
MAX_SCORE = 100
# 最低分, 低于该分值. 被删除
MIN_SCORE = 0

# 检测IP可用性
# 一次检测IP的数量
SEM_COUNT = 30
# 第一次启动的时候等待时间
START_VERIFY_WAIT_TIME = 10
