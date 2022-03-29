# dic = {}
# dic['jay'] = "周杰伦"  # 新key. 就新增
# dic['jay'] = "胡辣汤"  # 不可能有相同的key  相同的key会被覆盖掉
# print(dic)

# dic = {"name": "樵夫", "age": 18}

# v = dic['name']  # 根据key查询value的值
# print(v)

# 大多数情况下. 我们是知道key是什么的.
# v = dic['xxxx']  # KeyError: 'xxxx'
# v = dic.get("name")  # None, 至少不报错
# print(v)
#
# if dic.get("xxxx"):
#     存在
# else:
#     不存在

# 送给王婷
# "value" in list(dic.values())

# dic = {"name": "樵夫", "age": 18}
# for k in dic:
#     print(k)
#     print(dic[k])


dic = {
    "name": "汪峰",
    "age": 18,
    "wife": {
        "name": "章子怡",
        "age": 19,
    },
    "children": [
        {'name': "胡一菲", "age": 19},
        {'name': "胡二菲", "age": 18},
        {'name': "胡三菲", "age": 17},
    ]
}

# # 汪峰老婆的年龄
# age = dic['wife']['age']
# print(age)

# # 胡二非的年龄
# age = dic["children"][1]['age']
# print(age)

# 请获取到汪峰所有孩子的名字
for item in dic['children']:
    print(item['name'])
