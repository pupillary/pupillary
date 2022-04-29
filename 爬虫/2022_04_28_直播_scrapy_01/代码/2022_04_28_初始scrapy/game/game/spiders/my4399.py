import scrapy
m
# scrapy genspider name host
class My4399Spider(scrapy.Spider):  # 继承scrapy的Spider
    name = 'my4399'  # spider的名字
    # 限制该spider抓取的域名, 只要不符合该域名的一概过掉
    allowed_domains = ['4399.com']
    # 起始url, 在引擎开始工作的时候. 自动的包装成一个请求对象
    # 引擎进行调度. 交给下载器获取页面源代码,帮你封装成响应对象
    # 引擎把响应对象交给spider进行解析, 解析函数就是 下面的parse
    start_urls = ['http://www.4399.com/flash/gae100.htm']

    # 解析start_urls返回的响应
    # 不能乱改
    # 参数**kwargs 根据你的喜好进行增加 # 形参 => 变量
    # 不是我调用的. 是引擎自动调用.参数也是引擎自动传递
    def parse(self, resp, **kwargs):
        # resp: 响应对象
        # print(resp.text)  # 查看页面源代码
        # 插曲:settings.py设置 LOG_LEVEL, ROBOTSTXT_OBEY
        # 以前的做法
        # from lxml import etree
        # tree = etree.HTML(resp.text)
        # tree.xpath("xxx")
        # 现在的做法(scrapy中)
        li_list = resp.xpath("//*[@id='list']/li")  # parsel
        result = []
        for li in li_list:
            # extract() 提取内容的
            # [0]  ?? index out of range
            # name = li.xpath("./div[1]/a//text()").extract()
            # extract_first()  提取第一个, 它的好处是. 不会越界. 如果没有东西. 这里获取到的是None
            name = li.xpath("./div[1]/a//text()").extract_first()
            leibie = li.xpath("./span[1]/a/text()").extract_first()
            shijian = li.xpath("./span[2]/text()").extract_first()

            # print(name, leibie, shijian)

            # 给引擎返回数据, A OK   B NO
            # 拿到每一条数据, 拿一条. 返回一条. 最好???
            # yield 相当于临时的返回一个数据, 函数继续运行
            # 生成器函数 -> py基础
            # yield返回只能是以下内容:
            # 字典, item, 是数据,  去pipeline保存数据
            # request, 继续请求  去调度器的请求队列
            # None  结束
            yield {"name": name, "leibie": leibie, "shijian": shijian}
