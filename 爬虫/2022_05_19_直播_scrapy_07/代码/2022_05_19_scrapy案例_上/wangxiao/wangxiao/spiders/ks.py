import scrapy
import json


class KsSpider(scrapy.Spider):
    name = 'ks'
    allowed_domains = ['wangxiao.cn']
    start_urls = ['http://ks.wangxiao.cn/']

    def parse(self, resp, **kwargs):
        # 解析页面结构
        li_list = resp.xpath("//ul[@class='first-title']/li")
        for li in li_list:
            first_title = li.xpath("./p/span/text()").extract_first()
            a_list = li.xpath("./div/a")  # 所有二级类目
            for a in a_list:
                second_title = a.xpath("./text()").extract_first()
                second_href = a.xpath("./@href").extract_first()

                second_href = resp.urljoin(second_href)

                # http://ks.wangxiao.cn/TestPaper/list?sign=jz1  -> 模拟考试
                # http://ks.wangxiao.cn/exampoint/list?sign=jz1  -> 考点练习

                # 第一个方案, 可以访问 "模拟考试" url. 找到  "考点练习" 的url
                # 第二个方案, 可以直接replace
                second_href = second_href.replace("TestPaper", "exampoint")
                # print(first_title, second_title, second_href)

                # # 访问二级类目中的考点练习.
                # yield scrapy.Request(
                #     url=second_href,
                #     callback=self.parse_second,
                #     meta={
                #         "first_title": first_title,
                #         "second_title": second_title,
                #     }
                # )

                # 测试的时候. 定死访问 "一级建造师"
                yield scrapy.Request(
                    url="http://ks.wangxiao.cn/exampoint/list?sign=jz1",
                    callback=self.parse_second,
                    meta={
                        "first_title": "工程类",
                        "second_title": "一级建造师",
                    }
                )
                return  # 让整个parse. 暂停下来.

    def parse_second(self, resp, **kwargs):
        first_title = resp.meta['first_title']  # 自己思考. 为什么不用get?
        second_title = resp.meta['second_title']
        # print(first_title, second_title)
        # print(resp.url)

        a_list = resp.xpath("//div[@class='filter-item']/a")
        for a in a_list:
            third_title = a.xpath("./text()").extract_first()
            third_href = a.xpath("./@href").extract_first()
            third_href = resp.urljoin(third_href)
            yield scrapy.Request(
                url=third_href,
                callback=self.parse_third,
                meta={
                    "first_title": first_title,
                    "second_title": second_title,
                    "third_title": third_title
                }
            )
            break  # return 在这里没有区别

    def parse_third(self, resp, **kwargs):
        first_title = resp.meta['first_title']  # 自己思考. 为什么不用get?
        second_title = resp.meta['second_title']
        third_title = resp.meta['third_title']

        print(first_title, second_title, third_title)
        print(resp.url)

        chapter_items = resp.xpath("//div[@class='panel-content']/ul[@class='chapter-item']")
        for chapter in chapter_items:
            section_point_items = chapter.xpath(".//ul[@class='section-point-item']")
            if section_point_items:  # 拿子ul. 如果拿到了. 文件夹
                # section_point_item 最里层. 拿到 外层的外层的外层 -> chapter-item
                # 休息一下。 缓缓脑子。 回来开始蛋疼。
                for point_item in section_point_items:
                    # ancestor 从内层向外层查找元素
                    """
                    学校
                        一班
                            第一排
                                第一列ancestor-or-self::一班
                                第二列
                                第三列
                        二班
                            第一排
                        
                    """
                    points = point_item.xpath("./ancestor::ul[@class='section-item' or @class='chapter-item']")
                    # points => [德云社, 东北大区, 哈尔滨专区]
                    r = [first_title, second_title, third_title]
                    for point in points:  # 文件夹
                        p_name = "".join(point.xpath("./li[1]//text()").extract()).strip().replace(" ", "")  # 文字信息
                        r.append(p_name)
                    dir_path = "/".join(r)

                    # 自己的文件名称,
                    file_name = "".join(point_item.xpath("./li[1]//text()").extract()).strip().replace(" ", "")
                    print(dir_path, file_name)

                    top = point_item.xpath("./li[2]/text()").extract_first().split("/")[1]
                    sign = point_item.xpath("./li[3]/span/@data_sign").extract_first()
                    subsign = point_item.xpath("./li[3]/span/@data_subsign").extract_first()
                    data = {
                        "examPointType": "",
                        "practiceType": "2",
                        "questionType": "",
                        "sign": sign,
                        "subsign": subsign,
                        "top": top,
                    }
                    # 发送请求到listQuestions, 获取到题目
                    url = "http://ks.wangxiao.cn/practice/listQuestions"
                    yield scrapy.FormRequest(
                        url=url,
                        method="post",
                        body=json.dumps(data),  # 要的就是字符串.
                        callback=self.parse_questions,
                        headers={
                            "Content-Type": "application/json; charset=UTF-8"
                        },
                        meta={
                            "dir_path": dir_path,
                            "file_name": file_name
                        }
                    )
                    return   # 为了测试

            else:
                # 如果拿不到. 本身就是一个文件
                # 自己的文件名称,
                dir_path = "/".join([first_title, second_title, third_title])
                file_name = "".join(chapter.xpath("./li[1]//text()").extract()).strip().replace(" ", "")

                top = chapter.xpath("./li[2]/text()").extract_first().split("/")[1]
                sign = chapter.xpath("./li[3]/span/@data_sign").extract_first()
                subsign = chapter.xpath("./li[3]/span/@data_subsign").extract_first()
                data = {
                    "examPointType": "",
                    "practiceType": "2",
                    "questionType": "",
                    "sign": sign,
                    "subsign": subsign,
                    "top": top,
                }
                # 发送请求到listQuestions, 获取到题目
                url = "http://ks.wangxiao.cn/practice/listQuestions"
                yield scrapy.Request(
                    url=url,
                    method="post",
                    body=json.dumps(data),  # 要的就是字符串.
                    callback=self.parse_questions,
                    headers={
                        "Content-Type": "application/json; charset=UTF-8"
                    },
                    meta={
                        "dir_path": dir_path,
                        "file_name": file_name
                    }
                )
                return  # 为了测试
                pass  # 准备直接处理chapter即可

    def parse_questions(self, resp, **kwargs):
        # 文件夹, 文件名
        file_name = resp.meta['file_name']
        dir_path = resp.meta['dir_path']

        # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        # 这个错误只有一个解释. 你的本次请求. 拿到的东西. 不是json

        # print(resp.json())
        # 解决上述问题. 先resp.text. 确定好. 没有问题.
        print(resp.text)  # 解析这个json





        # 这里是否能拿到那一堆json


"""
requests  -> 

    get:
        Query String Parameters  ->  url
        url上拼接? xxx=xxx&xxxx=xxxx
        params -> 也可以把上述参数进行设置
    
    post:
        Form Data
            把字典传递个data即可
            requests.post(url, data=dict)
        Request Payload
            把字典处理成json传递给data
            字典处理成json之后. json是不是字符串????
            同时需要给出请求头中的Content-Type : application/json
"""

if __name__ == '__main__':
    import json

    dict = {
        "examPointType": "",
        "practiceType": "2",
        "questionType": "",
    }
    print(type(json.dumps(dict)))




