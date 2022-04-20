import pymysql
from pymysql.cursors import DictCursor

# 查询操作
# 1.  建立链接
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="luffycity"  # 连接的数据库
)
# 2. 创建cursor, 为了方便处理. 可以用DictCursor把数据进行格式化成[{}, {}]
cur = conn.cursor(DictCursor)

# 3. 准备sql
sql = "select * from men"
# 4. 执行sql,
r = cur.execute(sql)  # 查询的结果。 不是直接给到你的。

# 5. 获取结果
# one = cur.fetchone()  # 拿一个
# print(one)
#
# another = cur.fetchone()  # 拿一个，继续拿的话。 是接着拿
# print(another)
# all = cur.fetchall()
# for item in all:
#     print(item)
# 如果你想看到其他数据结构. 需要更换cursor
all = cur.fetchall()
print(all)
for item in all:
    print(item)

cur.close()  # 断开cursor
conn.close()  # 断开连接
