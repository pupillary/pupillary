import scrapy


class DengSpider(scrapy.Spider):
    name = 'deng'
    allowed_domains = ['17k.com']
    start_urls = ["https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"]

    # 需要先登录, 登录完成之后. 才开始start_urls
    def start_requests(self):
        # 完成登录的操作
        # scrapy想要发送POST请求：两种方式
        login_url = "https://passport.17k.com/ck/user/login"
        # 参数
        # loginName: 16538989670
        # password: q6035945
        # 发送post请求, 方案一
        # yield scrapy.Request(
        #     url=login_url,
        #     method="POST",  # post请求
        #     # 要求body的格式是下面这个格式. 这个格式http post请求的请求体
        #     # name=alex&age=18&xxx=123
        #     body="loginName=16538989670&password=q6035945",  # 注意,这里要求body是字符串
        #     callback=self.login_success
        # )
        # 发送post请求, 方案二
        yield scrapy.FormRequest(
            url=login_url,
            method="POST",
            formdata={  # 相当于requests.post(url, data={})
                "loginName": "16538989670",
                "password": "q6035945",
            },
            # 当前这个请求的url. 在得到响应之后. 要执行的函数
            callback=self.login_success
        )

    def login_success(self, resp, **kwargs):
        print(resp.text)
        # 登录成功之后. 需要请求到start_urls里面
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

    def parse(self, resp, **kwargs):
        print(resp.text)

    # 总结, 在scrapy中. 只要你需要发送请求了. 写yield scrapy.Request(url, callback=?)  # 一会儿用它
