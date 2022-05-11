# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from w3lib.http import basic_auth_header


# 快代理
# 账号:
# 18614075987
# 密码:
# q6035945

# tps365.kdlapi.com      15818
# tps366.kdlapi.com(备用)	15818
# 用户名：t14860877193391
# 密码：kg72z3rb
# 接下来找官方文档

class BaiduProxySpiderMiddleware:
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


class BaiduProxyDownloaderMiddleware:

    def process_request(self, request, spider):
        proxy = "tps365.kdlapi.com:15818"  # 更换个隧道
        request.meta['proxy'] = "http://%(proxy)s" % {'proxy': proxy}
        # 用户名密码认证
        request.headers['Proxy-Authorization'] = basic_auth_header('t14860877193391', 'kg72z3rb')  # 白名单认证可注释此行
        request.headers["Connection"] = "close"
        return None

    # 为什么樵夫把这个留在这里了？
    def process_response(self, request, response, spider):
        # 它不对劲的时候。 是不是应该重新发送请求
        # 可能需要在返回的时候. 做进一步的判断. 判断该次请求是否是理想中的响应体
        if "百度安全验证" in response.text:
            # 回去。 重新发送请求
            # 不需要去重
            request.dont_filter = True  # (调度器)不去重
            return request  # 发回重审
        return response

