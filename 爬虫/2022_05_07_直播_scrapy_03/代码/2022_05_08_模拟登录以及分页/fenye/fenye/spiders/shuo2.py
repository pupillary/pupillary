import scrapy


class Shuo2Spider(scrapy.Spider):
    name = 'shuo2'
    allowed_domains = ['17k.com']
    start_urls = ['https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html']

    def parse(self, resp, **kwargs):  # 解析第一页的逻辑
        trs = resp.xpath("//table/tbody/tr")
        for tr in trs:
            leibie = tr.xpath("./td[2]//text()").extract()
            mingzi = tr.xpath("./td[3]//text()").extract()
            zuozhe = tr.xpath(".//li[@class='zz']/a/text()").extract_first()
            print(leibie, mingzi, zuozhe)

        # 在解析完数据之后. 可以提取分页的url?
        hrefs = resp.xpath("//div[@class='page']/a/@href").extract()
        for href in hrefs:  # 2, 3, 4, 5, 2
            if href.startswith("javascript"):
                continue
            # print(href)  # 2, 3, 4, 5, 2

            href = resp.urljoin(href)
            # print(href)
            # # ??? 发送新的请求到
            # 1: 2, 3, 4, 5, 2,
            # 2: 1, 3, 4, 5, 6
            # 3: 1, 2, 4, 5, 6, 7
            #                   8
            # last:             334

            # scrapy, 调度器. 里面有一个set集合, 去除重复的url, 还有一个请求队列
            yield scrapy.Request(
                url=href,  # 2, 3, 4, 5, 6 的结果和1一样. 那么解析的时候. 是不是一样的逻辑 ????
                callback=self.parse,  # 7777  999 引擎
            )
