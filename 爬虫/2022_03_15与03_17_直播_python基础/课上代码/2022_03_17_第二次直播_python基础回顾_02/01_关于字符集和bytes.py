# s = "你们认识了"  # 当程序跑起来的时候
# 程序的运行是要消耗内存的
# 内存是软件运行时存储数据的一个地方 RAM
# 内存的作用是 给CPU的进行任务调度提供资源

# 内存和硬盘是不一样的.
# 你的程序中产生的字符串. 实际上运行的时候
# 要消耗内存的. 当程序运行完毕之后. 你当前程序
# 消耗的内存资源会被操作系统回收.

# 在python当中. 我们使用的字符串
# 在内存中是使用unicode码来存储
# unicode是不能进行存储到硬盘.
# 如果我需要进行存储的话.
# 需要把内存中的unicode进行一个编码
# 编码之后的东西才可以进行数据的永久存储和传输
# 不同的编码标准. 编码之后的结果是不一样的

# 全世界有非常多的编码方案
# 我们需要知道的就两个
# 1.中国人的自己设置的编码: GBK
# 2.全世界都统一的一套编码: UTF-8


# gbk, utf-8进行编码中文. 出来的结果一定是不一样的!!!!
# s = "今天看张三"
# gbk
# encode()  把字符串通过某种特定的字符集进行编码
# bs = s.encode("gbk")
# # b'\xbd\xf1\xcc\xec\xbf\xb4\xd5\xc5\xc8\xfd'
# print(bs)
# decode()  把已经编码好的字节，变回普通的字符串

# bs = b'\xbd\xf1\xcc\xec\xbf\xb4\xd5\xc5\xc8\xfd'
# s = bs.decode("gbk")
# print(s)

# encode(), decode()


# utf-8
# b'\xbd\xf1\xcc\xec\xbf\xb4\xd5\xc5\xc8\xfd'
# b'\xe4\xbb\x8a\xe5\xa4\xa9\xe7\x9c\x8b\xe5\xbc\xa0\xe4\xb8\x89'
# bs = s.encode("utf-8")
# print(bs)

# 不能乱来
# gbk 就用gbk解码
# utf-8 就用utf-8解码

# # b'abcdefg'
# # b'abcdefg'
# s1 = "abcdefg"
# print(s1.encode("utf-8"))
# print(s1.encode("gbk"))

# encode()  编码 -> 把字符串存储到硬盘的时候
# decode()  解码
# gbk     国标码
# utf-8   国际码
# s = b''  # 字节

# 硬盘上， 不一定存储的都是文字。
# 小片片。美图， 小姐姐，小音乐。xxx。exe => 字节
# 硬盘上所有的玩意。 都是字节(程序员需要知道的最小的数据单位)
