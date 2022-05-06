import scrapy
from urllib.parse import urljoin


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/dongman/']

    def parse(self, resp, **kwargs):  # scrapy自动执行这个parse -> 解析数据
        # print(resp.text)
        # 1. 拿到详情页的url
        a_list = resp.xpath("//*[@class='pic-list2  clearfix']/li/a")
        for a in a_list:
            href = a.xpath("./@href").extract_first()
            if href.endswith(".exe"):
                continue

            # href = urljoin(resp.url, href)  # 这个拼接才是没问题的.
            # print(resp.url)  # resp.url   当前这个响应是请求的哪个url回来的.
            # print(href)
            # 仅限于scrapy
            href = resp.urljoin(href)  # resp.url 和你要拼接的东西
            # print(href)
            # 2. 请求到详情页. 拿到图片的下载地址

            # 发送一个新的请求
            # 返回一个新的请求对象
            # 我们需要在请求对象中, 给出至少以下内容(spider中)
            # url  -> 请求的url
            # method -> 请求方式
            # callback -> 请求成功后.得到了响应之后. 如何解析(parse), 把解析函数名字放进去
            yield scrapy.Request(
                url=href,
                method="get",
                # 当前url返回之后.自动执行的那个解析函数
                callback=self.suibianqimignzi,
            )

    def suibianqimignzi(self, resp, **kwargs):
        # 在这里得到的响应就是url=href返回的响应
        img_src = resp.xpath("//*[@id='bigImg']/@src").extract_first()
        # print(img_src)
        yield {"img_src": img_src}



