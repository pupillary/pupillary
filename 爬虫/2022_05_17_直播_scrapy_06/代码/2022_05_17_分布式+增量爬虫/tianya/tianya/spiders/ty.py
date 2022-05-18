import scrapy
from scrapy import signals
from redis import Redis


# 去除重复
class TySpider(scrapy.Spider):
    name = 'ty'
    allowed_domains = ['tianya.cn']
    start_urls = ['http://bbs.tianya.cn/list.jsp?item=free&order=1']
    # 需要redis来去除重复的url
    # 先打开redis 先创建好连接

    # 用scrapy的方式来绑定事件
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def spider_opened(self, spider):  # 在这里建立连接
        self.conn = Redis(host="127.0.0.1", port=6379, password="123456", db=6)

    def spider_closed(self, spider):  # 关闭redis连接
        if self.conn:  # 好习惯
            self.conn.close()

    def parse(self, resp, **kwargs):
        tbodys = resp.xpath("//div[@class='mt5']/table/tbody")[1:]
        for tbody in tbodys:
            trs = tbody.xpath("./tr")
            for tr in trs:
                title = tr.xpath("./td[1]/a/text()").extract_first()
                href = tr.xpath("./td[1]/a/@href").extract_first()
                href = resp.urljoin(href)
                print(href)
                # 判断是否已经抓取过了, 如果已经抓取过了。 不再重复抓取了
                # 如果没有被抓取过。就会发送请求出去
                # "ty:urls" 大key
                t = self.conn.sismember("ty:urls", href)
                if t:
                    print("该数据已经被抓取过了。 不需要重复的抓取")
                else:
                    yield scrapy.Request(url=href, callback=self.parse_detail, meta={"href": href})
                    # 1 如果这一次请求没有成功？

        # 技术上的东西。 都在这里了。自己做做看 很久没有作业了, 做的时候，一定加上延迟.
        # 下一页， 请求3页
        # 找到下一页的链接
        # hh = "http://www.baidu.com"
        # yield scrapy.Request(url= hh, callback=self.parse, meta={"page": 变量})

    def parse_detail(self, resp, **kwargs):  # .  /   //
        href = resp.meta['href']  # href别手懒。 一定手工传递过来。 防止重定向的发生
        txts = resp.xpath("//div[@class='bbs-content clearfix']//text()").extract()  # 解析详情页的内容
        txt = "".join(txts)
        txt = txt.strip()
        # print(txt)
        # yield 给管道返回数据了 # 管道中出现错误的几率是小的。 可控的。
        # 2
        self.conn.sadd("ty:urls", href)
        # 管道 3
        # 数据去重
        yield {"content": txt}
