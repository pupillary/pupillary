# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 爬虫中间件, 最后看它
class ZhongSpiderMiddleware:
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


# 下载器中间件, 重点
class ZhongDownloaderMiddleware:
    # Not all methods need to be defined.
    # 下面给的这几个功能. 需要就留着. 不需要可以删掉
    # If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod  # 不用管
    def from_crawler(cls, crawler):  # 在创建spider的时候. 自动的执行这个函数
        # This method is used by Scrapy to create your spiders.
        # 在创建spider的时候. 自动的执行这个函数
        s = cls()  # 创建当前类的对象 -> 理解成每个函数中的self就可以了
        # s: self
        # singles: scrapy定义好的一些信号
        # scrapy的信号,链接(s.spider_opened, signal=signals.spider_opened)
        # 信号: 通信
        #  当触发了xxxx信号的时候. 自动运行某些东西
        #  火警报警器
        #  触发了烟雾信号, 自动放水
        # 相当于给引擎绑定一些功能
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.王力宏, signal=signals.spider_closed)
        return s

    def 王力宏(self, spider):
        pass


    # 必须知道, 处理请求的,  请求在发送给下载器的时候. 自动执行的函数. 正常情况下, 响应对象么?
    def process_request(self, request, spider):   # 拦截请求. 对请求对象进行处理.
        print("我要处理请求了。 我要上天")
        # Called for each request that goes through the downloader
        # middleware.
        # 参数:request, 就是当前请求

        # 小总结:
        # 引擎,如果接收到request, 走调度器
        # 引擎,如果接收到response, 走spider
        # 引擎,如果接收到item, dict, 走pipeline

        # return Must either: 返回值必须是以下的某一个
        # - None: 继续向后走,走到后面的中间件或者走到下载器
        # - Response object, 停下来. 这个请求就不会走下载器, 而是直接把响应对象给到引擎
        # - Request object, 停下来.这个请求也不会走下载器. 而是直接把请求对象给到引擎. 引擎继续走调度器。。
        return None

    # 必须知道
    # 处理响应的
    def process_response(self, request, response, spider):
        print("我要处理响应了。 我要处理cool")
        # Called with the response returned from the downloader.
        # 在响应对象反馈给引擎的时候自动执行, 可以判断各种状态码. 判断返回的数据是否正常.

        # Must either; 不能返回None
        # - return a Response object  把响应对象返回, 继续往回走
        # - return a Request object   返回一个请求对象,直接把请求发给引擎, 引擎继续走调度器。。。。
        return response


    # 在上述两个函数执行过程中.产生了异常. 自动运行process_exception
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhongDownloaderMiddleware_1:  # 997

    def process_request(self, request, spider):
        print("请求!!!!_1")

    def process_response(self, request, response, spider):
        print("响应!!!!_2")
        return response

class ZhongDownloaderMiddleware_2:  # 998

    def process_request(self, request, spider):
        print("请求!!!!_3")

    def process_response(self, request, response, spider):
        print("响应!!!!_4")
        return response
