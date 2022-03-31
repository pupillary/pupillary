import re

# 接下来的内容. 都是python提供的工具. 你需要记
# 查找所有
# 结果 = re.findall(正则, 字符串) => 返回列表（坑）
# r""专业写正则的。 没有转义的烦恼
# result = re.findall(r"\d+", "我有1000万，不给你花，我有1块我给你")
# print(result)

# # 结果 = re.finditer(正则, 字符串) => 返回迭代器(需要for循环)
# result = re.finditer(r"\d+", "我有1000万，不给你花，我有1块我给你")
# print(result)  # iterator  循环拿结果
# for it in result:  # <re.Match object; span=(2, 6), match='1000'>
#     # print(it)  # 从每一个Match里拿结果
#     print(it.group())  # group叫分组
# # finditer =》迭代器  =》循环 =>  match => group()


# # 结果 = re.search(正则，字符串), 全局搜索。 搜索到了。直接返回结果(返回第一个结果)
# r = re.search(r"\d+", "我有1000万，不给你花，我有1块我给你")
# print(r)  # <re.Match object; span=(2, 6), match='1000'>
# print(r.group())

# 多个相同格式的结果: finditer
# 单个格式的结果： search
# finditer search

# # compile： 加载
# obj = re.compile(r"\d+")  # 加载好一个正则表达式
# # result = obj.finditer("我叫王二麻子，我今年10岁了")
# # for it in result:
# #     print(it.group())
#
# r = obj.search("我爱你。100块随便爱")
# print(r.group())


# s = """
# hahah<div class='西游记'><span id='10010'>中国联通</span></div>
# <div class='三国杀'><span id='10086'>中国移动</span></div>heheh
# """
# # () 分组
# # ?P<名字>  给这一组起名字
# # 提取的时候就可以根据分组名字来提取具体数据
# obj = re.compile(r"<div class='(?P<jay>.*?)'><span id='(?P<id>.*?)'>(?P<lt>.*?)</span></div>")
#
# result = obj.finditer(s)
# for item in result:
#     print(item.group("jay"))  # .*? => 西游记|三国杀 7  9
#     print(item.group("id"))  # .*? => 西游记|三国杀 7  9
#     print(item.group("lt"))  # .*? => 西游记|三国杀 7  9
