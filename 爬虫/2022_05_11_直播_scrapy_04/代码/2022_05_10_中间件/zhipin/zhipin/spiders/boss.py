import scrapy
from zhipin.req import SeleniumRequest  # 导入自己的这个类

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=2&ka=page-2']

    def start_requests(self):
        # 要用selenium了
        # yield SeleniumRequest(url=self.start_urls[0], dont_filter=True)  # 1
        # yield scrapy.Request(url="http://www.qq.com", dont_filter=True)  # 2
        pass

    def parse(self, resp, **kwargs):
        print("我是parse", resp.url)
