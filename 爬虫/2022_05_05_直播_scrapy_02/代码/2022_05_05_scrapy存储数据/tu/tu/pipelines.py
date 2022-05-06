# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
# ImagesPipeline 图片专用的管道
from scrapy.pipelines.images import ImagesPipeline


class TuPipeline:
    def process_item(self, item, spider):
        print(item['img_src'])
        # 一个存储方案.
        # import requests
        # resp = requests.get(img_src)
        # resp.content
        return item

# scrapy的方案
class MyTuPipeline(ImagesPipeline):
    # 1. 发送请求(下载图片, 文件, 视频,xxx)
    def get_media_requests(self, item, info):
        url = item['img_src']
        yield scrapy.Request(url=url, meta={"sss": url})  # 直接返回一个请求对象即可

    # 2. 图片的存储路径
    # 完整的路径: IMAGES_STORE + file_path()的返回值
    # 在这个过程中. 文件夹自动创建
    def file_path(self, request, response=None, info=None, *, item=None):
        # 可以准备文件夹
        img_path = "dongman/imgs/kunmo/libaojun/liyijia"
        # 准备文件名字
        # 坑: response.url 没办法正常使用
        # file_name = response.url.split("/")[-1]  # 直接用响应对象拿到url
        # print("response:", file_name)
        file_name = item['img_src'].split("/")[-1]  # 用item拿到url
        print("item:", file_name)
        file_name = request.meta['sss'].split("/")[-1]
        print("meta:", file_name)

        real_path = img_path + "/" + file_name  # 文件夹路径拼接
        return real_path  # 返回文件存储路径即可

    # 3. 可能需要对item进行更新
    def item_completed(self, results, item, info):
        # print(results)
        for r in results:
            print(r[1]['path'])
        return item  # 一定要return item 把数据传递给下一个管道

