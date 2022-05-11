import scrapy
from scrapy.http.response.html import HtmlResponse


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']  # url写成这样. 避免重定向带给我们的错觉

    def parse(self, resp: HtmlResponse, **kwargs):
        print(resp.url)  # 响应回来之后. 我就打印一下url
