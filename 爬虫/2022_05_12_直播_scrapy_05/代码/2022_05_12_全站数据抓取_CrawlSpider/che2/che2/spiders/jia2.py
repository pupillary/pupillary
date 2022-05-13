import scrapy
from scrapy.linkextractors import LinkExtractor

# CrawlSpider: 可以实现全站数据提取, 是scrapy提供的一个爬虫
# 由于CrawlSpide做了高度的封装。 这个东西。 1. 不好理解， 2. 可控性比较差. 不作为重点学习。 了解即可.
class Jia2Spider(scrapy.Spider):
    name = 'jia2'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/']

    def parse(self, resp, **kwargs):
        # 提取链接用的
        lk1 = LinkExtractor(restrict_xpaths="//ul[@class='viewlist_ul']/li/a", deny_domains=("topicm.che168.com",))  # 提取详情页的url地址
        links = lk1.extract_links(resp)
        for link in links:
            url = link.url
            text = link.text
            # print(url)
        # 分页的连接提取
        lk2 = LinkExtractor(allow=r"beijing/a0_0msdgscncgpi1ltocsp\d+exx0")
        links = lk2.extract_links(resp)
        for link in links:
            print(link.url)
