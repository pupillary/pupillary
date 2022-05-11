import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    # 我希望每次请求都更换一个全新的User_agent
    def parse(self, resp, **kwargs):
        # 打印请求头
        print(resp.request.headers)
