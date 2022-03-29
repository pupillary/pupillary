# open() 打开
# gbk, utf-8
# 语法： open(文件路径, mode="模式", encoding="utf-8")
# 我打开了一个文件。 我想往里面写入一句话. "文字" -> 编码
# 我打开了一个文件。 我想从里面读出一句话. b"\x\x\x\x" -> 解码
# encoding： 在进行文本操作的时候。自动进行编码和解码

# 文件路径：相对于当前文件所在的文件夹。进行查找
# 模式：
# r, 只读。从文件里读取东西
# w, 只写。向文件写，如果文件存在，会清空， 如果不存在，创建文件。不创建文件夹
# a, 只追加写。
# b, 结合上面三个一起用的。 表示处理的是字节
#

# f = open("周杰.txt", mode="w", encoding="utf-8")  # 只有open的时候才会清理
# f.write("哈哈哈哈哈")  # 写入
# f.write("马化腾")  # 又写入 会不会清理掉
# f.close()

# No such file or directory: '周杰论.txt'
# open的时候。 不是把一个文件全部加载到内存
# open的内部你可以理解为， 有一个东西叫seek， 记录当前
# # 读取和写入的位置
# f = open("周杰论.txt", mode="r", encoding="utf-8")
# # content = f.read()  # 能读取到所有的内容
# # print(content)
# # hang1 = f.readline()
# # print(hang1)
#
# # 如果文件里有1538452
# # python中最佳的读取方案
# for line in f:  # 最好的。 记住了
#     print(line)
# # 养成好习惯。用完的文件。记得关闭
# f.close()

# # print里面有个换行
# print("hello world", end=" 哈哈哈哈哈 ")   # print里面有个东西帮我们进行了换行
# print("我爱你")


# # 回去敲。
# f = open("周杰论.txt", mode="r", encoding="utf-8")
# for line in f:  # 以后读取普通文本。 切记。第一件事儿。干掉换行
#     line = line.strip()  # 干掉空白 空格 \t \n \r
#     print(line)  # print里面有换行
#
# # print(f.readlines())
# print("over!!!!")

# # a： append 追加
# f = open("周杰伦.txt", mode="a", encoding="utf-8")
# f.write("青花瓷")
# f.write("\n")  # 换行
# f.write("千里之外")
# f.write("\n")

# # b，bytes 处理字节的
# # 小电影，图片， mp3， mp4。 exe
# # 非文本文件
# f = open("胡一菲.jpg", mode="rb") # 读取和写入非文本用b
# bs = f.read()
# print(bs)

# 聊聊with, 可以自动的关闭文件
# with open(xxxx) as f:  # 自动帮我们关闭文件
    # f.read()
    # for line in f:
    # f.write()
    # pass
# f.close()
# 处理一页数据
f = open("xxxx.txt", mode="w", encoding="gbk")
for i in range(10):  # 翻页， 10页
    f.write("数据1")
    f.write("数据2")
# 最后文件里。 只有最后一页的数据? open的位置是否有问题
