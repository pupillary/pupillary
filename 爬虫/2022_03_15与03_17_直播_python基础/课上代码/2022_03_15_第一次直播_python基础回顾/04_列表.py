# lst = []
# if lst:  # 要注意.
#     item = lst[0]  # IndexError: list index out of range
#     print(item)

# name = "周杰伦"
# s = "我喜欢{}".format(name)
# s1 = f"我喜欢{name}"

# for i in range(10):  # 0 1 2 3 4 5 6 7 8 9
#     print(i)

# for i in range(5, 10):  # 5 6 7 8 9
#     print(i)

# lst = ["赵本山", "周杰伦", "大嘴猴"]
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# for i in range(len(lst)):
#     print(lst[i])
#
# for i in range(len(lst)):
#     print(i, lst[i])  # 列表中每一项东西

# # for循环可以直接拿到列表中的每一项
# for item in lst:  # 拿到每一项数据, 没有索引.
#     print(item)

lst = ["jay", "alex", "wusir"]
# 把列表中所有的字母变成大写.
# 不好使
# for item in lst:
#     print(item.upper())
# print(lst)

# for i in range(len(lst)):  # 伴随着修改
#     lst[i] = lst[i].upper()
# print(lst)
