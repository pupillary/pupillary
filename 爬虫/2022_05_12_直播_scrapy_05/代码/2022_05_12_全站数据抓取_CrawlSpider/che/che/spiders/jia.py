import scrapy


class JiaSpider(scrapy.Spider):
    name = 'jia'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/']

    # 提前定义一个数据结构
    # 映射,  页面上的小标签和最终的数据key
    che_biaoqian = {  # 表显里程 3.5万公里
        # 页面上的标签名: "未来数据key的名字"
        "表显里程": "licheng",
        "上牌时间": "shijian",
        "挡位/排量": "pailiang",
        "车辆所在地": "suozaidi",
        "查看限迁地": "biaozhun",
    }  # 1

    def parse(self, resp, **kwargs):
        # print(resp.url)  # 做个测试。证明请求是通畅
        # 在这里。进行了详情页的连接的提取
        li_list = resp.xpath("//ul[@class='viewlist_ul']/li")
        for li in li_list:
            href = li.xpath("./a/@href").extract_first()

            href = resp.urljoin(href)
            if "topicm" in href:  # 过滤掉广告
                continue
            # print(href)
            # 发请求, 目的是为了拿到详情页的具体内容
            yield scrapy.Request(  # 把请求给了引擎。 至于是否到达了调度器？ 下载器？
                url=href,
                callback=self.parse_detail
            )
            # yield 请求1， yield 请求2， yield 请求3
            # 请求2被yield的时候。 请求1 不一定回来了
        # 分页逻辑了 在这里被执行的时候
        # print("我爱你")
        # 开始分页, 这里也是进行链接的提取
        hrefs = resp.xpath("//div[@id='listpagination']/a/@href").extract()
        for href in hrefs:
            # 判断字符串是否以xxx开头   startswith
            # 判断字符串中是否有xxxx    "xxxx" in s:
            # 判断字符串是否以xxxx结尾  endswith
            if href.startswith("javascript"):
                continue
            href = resp.urljoin(href)
            # 请求到分页url
            yield scrapy.Request(  # 提取的分页链接。 为了发送请求拿到下一页的内容
                url=href,
                # callback又走了自己一次。 是为了让下一页也执行完全相同的操作
                # 每一页都走了一遍第一页的流程
                callback=self.parse  # 这里不是递归。 像递归而已
            )

    # 只有这里能知道请求回来了, 回来的顺序。 也是无法保证的
    def parse_detail(self, resp, **kwargs):

        # 这里能被执行。 说明对详情页的请求回来了.
        # 解析详情页的内容了
        name = resp.xpath("//div[@class='car-box']/h3/text()").extract_first()
        print(name)
        li_list = resp.xpath("//div[@class='car-box']/ul/li")

        dic = {
            'licheng': '0公里',
            'shijian': '未知',
            'pailiang': '未知',
            'suozaidi': '地球',
            'biaozhun': '未知'
        }  # 2
        # 负责承载最终的数据
        # 可以考虑给出字典的默认值, 找defaultDict,或者手动给出默认值
        for li in li_list:  # 表显里程 3.5万公里, 车辆所在地 北京, 查看限迁地 欧V
            p_name = li.xpath("./p//text()").extract_first()
            p_value = li.xpath("./h4/text()").extract_first()
            # print(p_name, p_value)  # 表显里程 3.5万公里
            p_name = p_name.replace(" ", "").strip()  # 表显里程
            p_value = p_value.replace(" ", "").strip()

            data_key = self.che_biaoqian[p_name]  # licheng, shijian, dizhi, xxx
            dic[data_key] = p_value
        print(dic)  # 有可能缺少东西。 数据结构不够稳定。 pipeline可能会出现各种问题。 需要做很多次判断
        yield dic

        # 考虑分页
        # 拿urls
        # for u in urls:
        #   yield scrapy.Request(url=u, callback=self.parse_detail")

    # str， list， dict， set
    # 计算机程序 = 数据结构 + 算法


if __name__ == '__main__':
    pass
    # # 表显里程 3.5万公里
    # # 排量: 3.6
    # # 车辆所在地 北京
    # che_biaoqian = {  # 表显里程 3.5万公里
    #     # 页面上的标签名: "未来数据key的名字"
    #     "表显里程": "licheng",
    #     "上牌时间": "shijian",
    #     "挡位/排量": "pailiang",
    #     "车辆所在地": "suozaidi",
    #     "查看限迁地": "biaozhun",
    # }
    # che_biaoqian["表显里程"]  => "licheng"
    # che_biaoqian["车辆所在地"]  => "suozaidi"
    # che_biaoqian["排量"]  => "pailiang"
    # # shujv[che_biaoqian[p_name]] = p_value
    # shujv = {
    #     "licheng": "3.5",
    #     "shijian": "未知",
    #     "pailiang": "3.6",
    #     "suozaidi": "北京",
    #     "biaozhun": "未知",
    # }
