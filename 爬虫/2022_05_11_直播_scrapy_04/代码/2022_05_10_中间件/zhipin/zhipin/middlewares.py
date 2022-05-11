# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from scrapy.http.response.html import HtmlResponse

# 导入自己的包
from zhipin.req import SeleniumRequest


class ZhipinSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler): # 绑定信号
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.
        # 响应传递给spider的时候自动执行

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # 从spider返回到引擎的时候自动调用

        # Must return an iterable of Request, or item objects.
        for i in result:  # result就是spider中函数yield的东西的总和
            # i是每个结果
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
        # 第一次请求自动执行。 start_requests()
        # Must return only requests (not items).
        for r in start_requests:
            yield r  # 返回给引擎

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhipinDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.开始, signal=signals.spider_opened)
        crawler.signals.connect(s.结束, signal=signals.spider_closed)
        return s

    def 开始(self, spider):
        # 使用selenium来完成页面源代码(elements)的抓取
        # 无头自己加
        self.web = Chrome()  # 程序跑起来之后。 去创建Chrome对象。 程序跑完了之后。 关掉web对象
        self.web.implicitly_wait(10)  # 等待

    def 结束(self, spider):
        self.web.close()

    def process_request(self, req, spider):
        # isinstance: 判断xxxx是否是xxx类型的
        if isinstance(req, SeleniumRequest):
            print("我是selenium的")
            self.web.get(req.url)  # 直接访问即可
            self.web.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[3]/div/a[1]')  # 随便找个东西。如果找到了。就算加载完了
            page_source = self.web.page_source  # 就可以拿elements
            # 页面源代码有了？ 下载器还去么？
            # 组装一个响应对象。 返回 -> 引擎即可
            resp = HtmlResponse(  # 组装响应对象
                status=200,  # 状态码
                url=req.url,  # url
                body=page_source.encode("utf-8"),  # 页面源代码
                request=req  # 请求对象
            )
            return resp  # ?
        else:
            print(req.url)
            print("我是普通的")
            return None  # 正常放行。 正常走下载器那一套

    def process_response(self, request, response, spider):
        return response


