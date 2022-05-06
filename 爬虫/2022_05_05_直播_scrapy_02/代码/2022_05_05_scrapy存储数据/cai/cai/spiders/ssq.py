import scrapy
from cai.items import CaiItem  # pycharm的误报.
# CaiItem: 规范数据结构.每一条数据对应一个CaiItem


class SsqSpider(scrapy.Spider):
    name = 'ssq'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://match.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs']

    """
    1. 看你要的东西. 在不在页面源代码??????
    """
    def parse(self, resp, **kwargs):
        # print(resp.text)
        # 解析出. 你需要的数据
        trs = resp.xpath("//*[@id='cpdata']/tr")
        for tr in trs:
            red_ball = tr.xpath("./td[@class='chartball01' or @class='chartball20']/text()").extract()
            if not red_ball:  # 干掉空值
                continue
            # print(red_ball)

            blue_ball = tr.xpath("./td[@class='chartball02']/text()").extract_first()
            qi = tr.xpath("./td[1]/text()").extract_first()
            # print(qi, red_ball, blue_ball)
            # spider中可以返回字典
            # 在scrapy中, 官方并不推荐你返回数据的时候. 直接返回字典, 因为字典没有约束
            # 官方推荐使用Item来约束数据结构. 提前定义好这个结构
            # 用起来和字典几乎一样
            cai = CaiItem()  # 创建一个对象。 负责数据的存储
            cai['qi'] = qi
            cai['blue_ball'] = blue_ball
            cai['red_ball'] = red_ball

            yield cai

            # yield {
            #     "qi": qi,
            #     "red_ball": red_ball,
            #     "blue_ball": blue_ball
            # }  # 返回到哪里了？ 我在哪儿能拿到这些数据？？？？


