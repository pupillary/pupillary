# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo

# 120
class CaiPipeline:
    # 希望。 在程序跑起来的时候。打开一个w模式的文件
    # 在获取数据的时候正常写入
    # 在程序结束的时候。 关闭f

    # 仅限于pipeline固定的写法.
    # open_spider, 爬虫在开始的时候。 执行
    def open_spider(self, spider_name):
        self.f = open("xxx.csv", mode="w", encoding="utf-8")

    # close_spider, 爬虫结束的时候。 执行
    def close_spider(self, spider_name):
        self.f.close()

    # process_item 的作用就是接受spider返回的数据
    # spider每次返回一条数据. 这里都会自动的执行一次process_item
    # 数据以参数的形式传递过来. item
    def process_item(self, item, spider):
        # print(spider.name)
        # print("这里是管道", item['qi'], item['blue_ball'], item['red_ball'])
        # 存储数据，文件, mysql, mongodb, redis
        self.f.write(item['qi'])
        self.f.write(",")
        self.f.write("_".join(item['red_ball']))
        self.f.write(",")
        self.f.write(item['blue_ball'])
        self.f.write("\n")
        # self.f.close()  # 这里不能写
        return item   # return在process_item中的逻辑, 是将数据传递给一下管道

# 存MySQL
# 准备表. 创建好表.
# 150
class MySQLPipeline:
    def open_spider(self, spider_name):
        # 连接mysql
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            database="cai",
            user="root",
            password="root"
        )

    def close_spider(self, spider_name):
        self.conn.close()

    def process_item(self, item, spider):
        # 存储数据
        try:  # 代码调试期间. 可以考虑不添加try...except...为了能看到更加完整的错误信息
            cur = self.conn.cursor()
            qi = item['qi']
            # red_ball = "_".join(item['red_ball'])
            red_ball = item['red_ball']
            blue_ball = item['blue_ball']
            sql = f"insert into ssq(qi, red_ball, blue_ball) values ('{qi}', \"{red_ball}\", '{blue_ball}')"
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            if cur:
                cur.close()
            self.conn.rollback()
        # item['red_ball'] = "1234456"
        return item

# 存MongoDB
# 180
class MongoPipeline:
    def open_spider(self, spider_name):
        self.conn = pymongo.MongoClient(
            host="127.0.0.1",
            port=27017
        )
        self.db = self.conn['python']

    def close_spider(self, spider_name):
        self.conn.close()

    def process_item(self, item, spider):
        # print("mongo===>", item)
        # #  ???
        self.db.ssq.insert_one({"qi": item['qi'], "red_ball": item['red_ball'], "blue_ball": item['blue_ball']})
        return item  # 给到下一个管道
