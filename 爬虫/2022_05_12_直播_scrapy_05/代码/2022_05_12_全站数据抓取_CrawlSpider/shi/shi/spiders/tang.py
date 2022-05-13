import scrapy
from scrapy.linkextractors import LinkExtractor  # 链接提取器
from scrapy.spiders import CrawlSpider, Rule


class TangSpider(CrawlSpider):
    name = 'tang'
    allowed_domains = ['shicimingjv.com']
    start_urls = ['https://www.shicimingjv.com/tangshi/index_1.html']  # => parse

    # 省略了parse
    # 详情页的url地址
    lk1 = LinkExtractor(restrict_xpaths="//div[@class='sec-panel-body']/ul/li/div/h3/a")
    lk2 = LinkExtractor(restrict_xpaths="//ul[@class='pagination']/li/a")
    # rules
    rules = (
        # 这里crawlspider会自动提取链接， 并自动发送请求
        Rule(lk1, callback='parse_item'),
        # 把刚才的逻辑在来一遍
        # lk2 能够拿到-》 2.html, 3.html...4.5.6
        Rule(lk2, follow=True),  # follow: 表示是否继续重新来一遍 =>前面的callback=self.parse
    )

    # crawlspider的执行过程
    # def parse(self, resp, **kwargs):
    #     for r in self.rules:
    #         links = r.link_extractor.extract_links(resp)
    #         for link in links:
    #             url = link.url
    #             yield scrapy.Request(url=url, callback=r.callback)

    # 不是parse了。 换成parse-item
    def parse_item(self, response, **kwargs):
        # 解析详情页的内容
        title = response.xpath("//h1[@class='mp3']/text()").extract_first()
        print(title)

    # set集合, sha1, md5, sha256, sha512