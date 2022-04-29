# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GamePipeline:  # 保存数据的
    # process_item: 在引擎得到数据后. 进行数据类型判断之后. 如果是数据.
    # 引擎会自动的调用pipeline中的process_item函数
    # item, 就是数据
    # spider, 数据是从哪个爬虫穿过来的???
    def process_item(self, item, spider):
        print("我是pipeline, 我接收到了", item)

        return item
