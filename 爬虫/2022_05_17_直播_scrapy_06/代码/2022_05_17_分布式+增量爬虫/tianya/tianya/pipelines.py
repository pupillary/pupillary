# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from redis import Redis


class TianyaPipeline:

    def open_spider(self, spider):
        self.conn = Redis(host="127.0.0.1", port=6379, password="123456", db=6)

    def close_spider(self, spider):
        if self.conn:  # 好习惯
            self.conn.close()

    def process_item(self, item, spider):
        content = item['content']
        # redis
        if self.conn.sismember("ty:pipeline", content):
            print("已经有了。 不需要重复存储")
        else:
            self.conn.sadd("ty:pipeline", content)
            print("之前没有， 现在有了")
        return item
