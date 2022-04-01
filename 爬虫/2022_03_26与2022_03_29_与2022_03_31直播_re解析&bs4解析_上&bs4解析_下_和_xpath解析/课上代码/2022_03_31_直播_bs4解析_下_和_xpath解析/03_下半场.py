from lxml import etree

# 准备一段html
f = open("index.html", mode="r", encoding="utf-8")
content = f.read()

page = etree.HTML(content)


# 我要周大强
# 属性上的限定
# xpath语法中 @属性
# z = page.xpath("//ol/li[@id='10086']/text()")
# print(z)
#
# z = page.xpath("//li[@id='10086']/text()")
# print(z)
#
# # 这里写属性选择的时候. 直接复制即可(页面源代码).
# j = page.xpath("//li[@class='jay haha']/text()")
# print(j)
#
# # * 单个任意标签
# x = page.xpath("//*[@ygl='杜景泽']/text()")
# print(x)

# z = page.xpath("//div/*/span/text()")
# print(z)
#
# # 拿到ul中每一个href
# # @href 拿href的值
# # 方案一. A
# href = page.xpath("//ul/li/a/@href")
# for h in href:
#     print(h)
#     # 后续的操作。和该页面没有其他关系了
#     # 此时直接拿href没问题!!
#
#
# # 方案二. B 可扩展性更好一些。
# a_list = page.xpath("//ul/li/a")
# for a in a_list:
#     href = a.xpath("./@href")[0]
#     txt_lst = a.xpath("./text()")
#
#     if txt_lst:  # 判断
#         txt = txt_lst[0]
#     else:
#         txt = ""
#     # 需要把文字和href写入文件
#     print(txt, href)  # index out of range

# # last() 最后一个
# li = page.xpath("//ol/li[last()]/a/@href")
# print(li)
