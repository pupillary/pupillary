# pip install pymongo
import pymongo

# 1.连接
conn = pymongo.MongoClient(host="localhost", port=27017)
# 2.选择数据库
db = conn['python_4']  # use python_4
# 3. 开始操作
# db.stu.insert_one({"name": "alex"})
# pymongo     <=>  mongodb
# insert_one  <=>  insertOne
# 下划线命名    <=>  驼峰命名

# 为什么? 汪峰写10遍
# db.stu.insert_many([{name: "sylar"}, {"name": "tory"}, {"name": "relay"}])

# 查询
result = db.stu.find({}, {"_id": 0, "name": 1})
# print(dir(result))
for item in result:
    print(item)
print(dir(str))
