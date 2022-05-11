# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from baidu_ua.settings import User_Agents, PROXIES
import random  # 随机模块


class BaiduUaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaiduUaDownloaderMiddleware:

    def process_request(self, request, spider):
        # 先拿到所有的User—Agent
        # 随机抽选一个
        # 放到请求对象中
        # 返回什么》 处理完之后。 打算让它往哪儿走?? 引擎？ 下载器?
        ua = random.choice(User_Agents)
        # 设置请求头
        request.headers['User-Agent'] = ua
        return None  # ??


class BaiduUaDownloaderMiddleware_proxy:

    def process_request(self, request, spider):
        # 先拿到所有的User—Agent
        # 随机抽选一个
        # 放到请求对象中
        # 返回什么》 处理完之后。 打算让它往哪儿走?? 引擎？ 下载器?
        ip = random.choice(PROXIES)
        # 放代理
        request.meta['proxy'] = ip
        # 隧道代理（收费）

        return None  # ??




















