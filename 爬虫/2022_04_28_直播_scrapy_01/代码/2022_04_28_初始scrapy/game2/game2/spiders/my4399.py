import scrapy
from scrapy.http.response.html import HtmlResponse


class My4399Spider(scrapy.Spider):
    name = 'my4399'
    allowed_domains = ['4399.com']
    start_urls = ['http://www.4399.com/flash/game100.htm']

    def parse(self, resp: HtmlResponse, **kwargs):
        print(type(resp))

        # li_list = resp.xpath("//*[@id='list']/li")
        # for li in li_list:
        #     name = li.xpath("./div[1]/a//text()").extract_first()
        #     leixing = li.xpath("./span[1]/a/text()").extract_first()
        #     shijian = li.xpath("./span[2]/text()").extract_first()
        #     yield {"name": name, "leixing": leixing, "shijian": shijian}
