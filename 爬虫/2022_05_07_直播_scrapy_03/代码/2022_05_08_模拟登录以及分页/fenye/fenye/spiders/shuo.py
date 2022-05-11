import time

import scrapy


class ShuoSpider(scrapy.Spider):
    name = 'shuo'
    allowed_domains = ['17k.com']
    start_urls = ['https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html']

    def start_requests(self):  # scrapy是协程. 太快了
        for i in range(1, 10):
            url = f"https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{i}.html"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, resp, **kwargs):
        # print(resp.text)
        trs = resp.xpath("//table/tbody/tr")
        for tr in trs:
            leibie = tr.xpath("./td[2]//text()").extract()
            mingzi = tr.xpath("./td[3]//text()").extract()
            zuozhe = tr.xpath(".//li[@class='zz']/a/text()").extract_first()
            print(leibie, mingzi, zuozhe)


