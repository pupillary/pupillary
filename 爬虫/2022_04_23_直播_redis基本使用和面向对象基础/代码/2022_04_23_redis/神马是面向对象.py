# 生活当中. 我们操纵, 指示, 命令 生活当中的人来帮我们做事情
# 我们操纵的. 指挥的, 命令的那个东西就是对象
# 我们指挥对象去工作. 去做一些事情. 这个思维叫面向对象

# 我们之前写的东西. 是以我为中心. 写代码的逻辑是以流程为核心. 面向过程

# def get_page_source():
#     pass
#
# def jiexi():
#     pass
#
# if __name__ == '__main__':
#     resp = get_page_source()

# 得有对象. 才能指挥对象去干活
# 在编程的世界里. 你是上帝. 只有你. 所有的东西得有你来创造
# 由你来指挥

# 图纸 -> 你是上帝. 你怎么定义都行
# 类: 归类. 归纳
# class NvPengYou:  # 心里想的是帮我那杯水
#
#     # 在创建对象的时候. 我希望给该对象传递一些信息
#     # 保存下来
#     # 双下划线开头和结尾的东西。 都是特殊方法。 有特殊的访问方式
#     # self: 当前正在执行该动作的那个对象, 自动传递。不用管
#     def __init__(self, nickname, age, height, weight):
#         # 对象是谁？
#         # 是一个公共的地方
#         print("self", self)
#         print(age, height, weight)  # 参数可以传进来了
#         # 给对象添加一些变量信息。 这些信息会写入在对象的内存空间
#         self.nickname = nickname
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def nashui(self):  # 函数:对一段功能的封装
#         print(self.nickname, self.weight, self.height, "高高兴兴的")
#         print("给老公拿水")
#
#     def daoxijiaoishui(self):  #  p1.daoxijiaoshui()  p2.daoxijiaoshui()
#         print(self.nickname, "开开心心的倒洗脚水")  # ???? 对， 不对
#
#     def qinqin(self):
#         print(self.nickname, "亲情抱抱举高高")
#
#
#
# if __name__ == '__main__':  # 这就是你, 写代码
#     # # 得造女朋友  -> 会拿水
#     # # 生活当中. 造车~, 想办法先画图纸, 造车
#     p1 = NvPengYou("小贝", 18, 185, 50)  # 创建对象 类() => init()
#     # p1是对象, 对象能干什么事儿??? 图纸上写了什么. 就能干什么
#     p1.daoxijiaoishui()  # 对象.功能()
#     # # p1.chifan()  # 图纸上没有的功能. 不能执行
#     # # 类决定了造出来的对象. 能执行哪些功能
#     #
#     p2 = NvPengYou("消磨人", 20, 173, 50)  # 新女朋友
#     p2.daoxijiaoishui()
#     # # p1和p2 拥有各自独立的内存空间
#     # # p1和p2共享的是同一个类的空间, 有相同的功能
#     # print(id(p1))
#     # print(id(p2))
#     # # p1和p2是不是一个东西
#     #
#     # # lst = list()  # []
#     # # lst2 = list()  # []
#     # # lst.append(123)
#     # # print(lst2)
#
#
#
#
#     # 让对象去干活, 拿杯水
#


# class Girl:
#     def __init__(self, name, age):  # init 初始化
#         self.name = name
#         self.age = age
#
#     def daoshui(self):
#         print(self.name, "把水倒了")
#
#     def roujian(self):
#         print(self.name, "揉肩")
#
#     def zhihui(self):
#         for i in range(3):
#             # 每件事儿干三遍
#             # A 行， B, 不行
#             # 先倒水
#             self.daoshui()
#             # 揉肩
#             self.roujian()
#
#
# if __name__ == '__main__':
#     p1 = Girl("alex", 99)
#     p1.zhihui()
#
#     p2 = Girl("吴佩琦", 199)
#     p2.zhihui()

# self: 当前正在执行该动作的那个对象, 自动传递。不用管
class Animal:  # 动物
    def __chi(self):  # 私有的
        print("吃饭")
    def dong(self): # 公开的
        print("会动")  # B

    def run(self):
        self.dong()  # self:d
        # d.dong()  # d -> Dog
    # a.b()   a类型的 ->  b()
# 继承, 子类会自动的拥有父类中（除了私有内容）的所有内容
class Dog(Animal):  # 狗, 狗是一种动物
    def jiao(self):
        print("会汪汪")
    def dong(self):
        print("我是狗。 我会蛄蛹")  # A

class Cat(Animal):  # 猫， 猫是一种动物  x是一种y的时候, x可以继承y
    def haojiao(self):
        print("会喵喵")

if __name__ == '__main__':
    d = Dog()  # d => Dog
    # d.run()  # d.xxx  => Dog
    d.__chi()
