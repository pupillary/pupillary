import scrapy
from scrapy_redis.spiders import RedisSpider


# 之前我们scrapy定了版本了 2.5.1
# 安装 scrapy-redis == 0.7.2 版本
# 1. 改造spider
class Ty2Spider(RedisSpider):
    name = 'ty2'
    allowed_domains = ['tianya.cn']
    # start_urls = ['http://bbs.tianya.cn/list.jsp?item=free&order=1']
    # 2.准备启动url
    redis_key = "ty2:urls"  # 启动url

    def parse(self, resp, **kwargs):
        tbodys = resp.xpath("//div[@class='mt5']/table/tbody")[1:]
        for tbody in tbodys:
            trs = tbody.xpath("./tr")
            for tr in trs:
                title = tr.xpath("./td[1]/a/text()").extract_first()
                href = tr.xpath("./td[1]/a/@href").extract_first()
                href = resp.urljoin(href)
                yield scrapy.Request(url=href, callback=self.parse_detail, meta={"href": href})

    def parse_detail(self, resp, **kwargs):  # .  /   //
        href = resp.meta['href']  # href别手懒。 一定手工传递过来。 防止重定向的发生
        txts = resp.xpath("//div[@class='bbs-content clearfix']//text()").extract()  # 解析详情页的内容
        txt = "".join(txts)
        txt = txt.strip()
        print(txts)  # 看看效果
        yield {"content": txt}
