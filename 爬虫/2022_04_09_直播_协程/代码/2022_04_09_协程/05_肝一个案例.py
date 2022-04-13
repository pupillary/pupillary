import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import os

# 1. 拿到主页面的源代码 (不需要异步)
# 2. 拿到页面源代码之后. 需要解析出 <卷名>, <章节, href>
# 3. xxxxx

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}


def get_chaptor_info(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "UTF-8"
    page_source = resp.text
    # 开始解析
    tree = etree.HTML(page_source)
    """
    [  # 扩展思维..
    {"juan_name":"万国来朝", "chapters":[{"chapter_name": "第一章", "chapter_url": 'href'}, {}, {}]}, 
    {}, 
    {}, 
    {}, 
    {}, 
    {}]
    
    [
    {"juan_name":"万国来朝", "chapter_name": "第一章", "chapter_url": href}
    {"juan_name":"万国来朝", "chapter_name": "第二章", "chapter_url": href}
    {"juan_name":"万国来朝", "chapter_name": "第三章", "chapter_url": href}
    ....
    {"juan_name":"最后一部", "chapter_name": "第一章", "chapter_url": href}
    ]
    """
    # 作业, 请解释出每个循环在这里的作用?
    result = []
    divs = tree.xpath("//div[@class='mulu']")  # 每一个div就是一卷
    for div in divs:
        trs = div.xpath(".//table/tr")  # 一堆tr
        juan_name = trs[0].xpath(".//a/text()")
        juan_name = "".join(juan_name).strip().replace("：", "_")

        for tr in trs[1:]:  # 93

            tds = tr.xpath("./td")
            for td in tds:
                txt = td.xpath(".//text()")
                href = td.xpath(".//@href")

                txt = "".join(txt).replace(" ", "").strip()
                href = "".join(href)
                dic = {
                    "chapter_name": txt,
                    "chapter_url": href,
                    "juan_name": juan_name
                }
                result.append(dic)
    return result


async def download_one(url, file_path):
    print("我要下載文章了")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            page_source = await resp.text(encoding="utf-8")
            # 拿到文章
            tree = etree.HTML(page_source)
            content = tree.xpath("//div[@class='content']//p//text()")
            content = "".join(content).replace("\n", "").replace("\r", "").replace(" ", "").strip()

            # 寫入文件
            async with aiofiles.open(file_path, mode="w", encoding="utf-8") as f:
                await f.write(content)

    print("恭喜你。 下載了一篇文章!",file_path)


async def download_chapter(chaptor_list):
    tasks = []
    for chaptor in chaptor_list:  # {juan: xxx, name:xxx, href: xxx}
        juan = chaptor['juan_name']    # 文件夹名
        name = chaptor['chapter_name']  # 文件名  前言.txt
        url = chaptor['chapter_url']  # 用来下载 -> 异步任务

        if not os.path.exists(juan):  # 判斷文件夾是否存在
            os.makedirs(juan)  # 如果不存在就創建

        # 給出文件的真正的保存路徑
        file_path = f"{juan}/{name}.txt"  # 74
        f = download_one(url, file_path)
        t = asyncio.create_task(f)
        tasks.append(t)
        break  # 测试的时候
    await asyncio.wait(tasks)


def main():
    url = "https://www.mingchaonaxieshier.com/"
    chaptor_list = get_chaptor_info(url)
    # print(chaptor_list)
    # 开始上协程. 进行异步下载
    asyncio.run(download_chapter(chaptor_list))


if __name__ == '__main__':
    main()
