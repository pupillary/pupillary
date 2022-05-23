# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
import os   # python去和操作系统对接, 文件夹
from scrapy.pipelines.images import ImagesPipeline
from lxml import etree


class WangxiaoPipeline:
    def process_item(self, item, spider):  # 写入markdown  之前处理(A), 之后处理(B)
        # print(item)   # 怼到md文件中. 既能保留页面格式， 也能保留图片效果
        # question_info => <img src="http://www.baidu.com"/>
        # 文件和文件夹
        dir_path = item['dir_path']  # None[xxxx]
        file_name = item['file_name']

        # 需要判断一下. 如果这个文件夹存在了就不需要创建了. 如果不存在则创建
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # 一定有文件夹的
        real_path = dir_path + "/" + file_name + ".md"

        f = open(real_path, mode="a", encoding="utf-8")
        f.write(item['question_info'])
        f.write("\n")
        f.write("\n")
        f.close()

        return item


class WangxiaoImagePipeline(ImagesPipeline):  # IMAGES_STORE

    def get_media_requests(self, item, info):  # ?? A 发送下载的请求的
        # 图片的地址
        # item['question_info'] -> 图片的路径, xpath, bs4, re
        tree = etree.HTML(item['question_info'])
        srcs = tree.xpath("//img/@src")
        for src in srcs:  # 10张图片
            yield scrapy.Request(
                url=src,
                dont_filter=True,
                meta={
                    "src": src,
                    "dir_path":item['dir_path'],
                    "file_name": item['file_name']
                }
            )

    def file_path(self, request, response=None, info=None, *, item=None):  # 路径
        # 拼接路径
        dir_path = request.meta['dir_path']
        file_name = request.meta['file_name']
        src = request.meta['src']
        real_file_name = src.split("/")[-1]
        # 文件夹的路径
        return dir_path + "/" + file_name + "_imgs2" + "/" + real_file_name

    def item_completed(self, results, item, info):  # 收尾
        # 需要  src, 图片真正的存储路径
        # print(results)  # []
        for r in results:
            status = r[0]
            dic = r[1]
            if status:
                # 下载成功了. 可以进行替换了
                src = dic['url']
                path = dic['path']
                # 工程类/一级建造师/建设工程经济/1Z101000工程经济/1Z101010资金时间价值的计算及应用/1Z101011利息的计算/一、资金时间价值的概念_imgs2/dd1d502b-6786-44ad-a9c1-54b7649038b7.png
                xiao_list = path.split("/")[-2:]
                real_path = xiao_list[0] + "/" + xiao_list[1]
                item['question_info'] = item['question_info'].replace(src, real_path) # 7 9

        return item
