from lxml import etree
# import lxml
# etree = lxml.etree

# 准备一段html
f = open("index.html", mode="r", encoding="utf-8")
content = f.read()  # 页面源代码  # type: xxxxxx

# 1.      etree.HTML(页面源代码) BeautfulSoup(页面源代码)
page = etree.HTML(content)  # type: etree._Element # 给pycharm看的 # 默认pycharm不知道什么类型. 没有代码提示
# 2. xpath()  # 筛选
# page.xpath("?????")
# print(main_page)
# print(type(main_page))   # <class 'lxml.etree._Element'>
# main_page

# 以后写代码. 没提示怎么办?
# 用type() 得到数据类型.
# 去变量被赋值位置, 添加  # type: 类型

# 语法1, 根节点
# / 出现在开头. 表示根节点
# xpath得到的结果永远永远是列表
# root = page.xpath("/html")  # [<Element xxx at xxx>]
# print(type(root))

# / 出现在中间 直接子节点
# p = page.xpath("/html/body/div/p")
# print(p)   # type(p) ????

# / 出现在中间 也有可能是找某个节点内部的东西
# text() 提取内部的文本
# s = page.xpath("/html/body/div/p/text()")  # []
# print(s)  # ['一个很厉害的人']

# # // 提取的后代节点
# s = page.xpath("/html/body/div/p//text()")
# print(s)

# # // 查找所有子节点 /p 所有子节点中的p
# divs = page.xpath("//div/p/text()")
# print(divs)

# # 在xpath里 [] 里面可以给出位置. 位置是从1开始数的
# zi = page.xpath("//ol/ol/li[2]/text()")
# print(zi)

# # li[3] 表示 上层标签中第三个li
# r = page.xpath("//li[3]/text()")
# print(r)  # ?



