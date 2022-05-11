from scrapy.cmdline import execute


if __name__ == '__main__':
    # 也可以像这样来运行scrapy的程序.
    # 在这里运行的好处是:可以开启调试功能.
    # 程序就回到了我们熟悉的样子
    # execute("scrapy crawl baidu".split())
    execute(["scrapy", "crawl", "baidu"])

