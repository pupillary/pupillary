# 需求: 文章标题, 来源, 作者, 时间, 内容

# http://www.animationcritics.com/chinese_aniamtion.html

# 1. 在首页中获取到10个详情页的url地址.
# 经过循环.拿到每一个url地址
# 2. 访问详情页的url. 得到详情页的内容
# 3. 在详情页内容中提取到最终你需要的内容
#
# 你要的东西在页面源代码里??

import requests
import re
import time


url = "http://www.animationcritics.com/chinese_aniamtion.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}
resp = requests.get(url, headers=headers)  # 发请求
main_page_source = resp.text  # 字符串, 得到页面源代码

# re.S 让.能匹配换行
main_obj = re.compile(r'<li style="margin-bottom:10px;">.*?href="(?P<url>.*?)" title="(?P<title>.*?)"', re.S)

# 来源的正则
laiyuan_obj = re.compile(r"来源:</span>(?P<laiyuan>.*?)</span>", re.S)
zuozhe_obj = re.compile(r"作者:</span>(?P<zuozhe>.*?)</span>", re.S)
pub_data_obj = re.compile(r"发布时间: </span>(?P<pub_date>.*?)</span>", re.S)

section_obj = re.compile(r"<section.*?>(?P<content>.*?)</section>", re.S)
p_obj = re.compile(r"<p data-track=.*?>(?P<content>.*?)</p>", re.S)

content_filter_obj = re.compile(r"<.*?>", re.S)


# 匹配东西
result = main_obj.finditer(main_page_source, re.S)
for item in result:  # 每次循环得到一条匹配的结果
    child_url = item.group("url")  # 详情页url
    child_title = item.group("title")  # 标题
    # print(child_title, child_url)

    # 访问详情页
    child_resp = requests.get(child_url, headers=headers)
    child_page_source = child_resp.text
    # print(child_page_source)

    # 对详情页进行数据提取
    lyr = laiyuan_obj.search(child_page_source)   # search的结果是match对象.
    if lyr:  # 判空操作
        laiyuan = lyr.group("laiyuan")   # 需要group拿结果
    else:
        laiyuan = ""
    # print(laiyuan)

    # 作者
    zz_r = zuozhe_obj.search(child_page_source)
    if zz_r:
        zuozhe = zz_r.group("zuozhe")
    else:
        zuozhe = ""

    pub_data_r = pub_data_obj.search(child_page_source)
    if pub_data_r:
        pub_data = pub_data_r.group("pub_date")
    else:
        pub_data = ""

    print(child_title, laiyuan, zuozhe, pub_data)

    # 内容怎么搞??
    # 拿所有section中的内容
    sec_list = []
    section_results = section_obj.finditer(child_page_source, re.S)

    for section in section_results:
        content = section.group("content")
        sec_list.append(content)  # 把拿到的section的内容放到列表中

    all_content = "".join(sec_list)  # 拼接所有的section为一个字符串

    if not all_content:  # 如果是空. 用 p_obj 重新提取
        section_results = p_obj.finditer(child_page_source, re.S)
        for section in section_results:
            content = section.group("content")
            sec_list.append(content)  # 把拿到的section的内容放到列表中
        all_content = "".join(sec_list)  # 拼接所有的section为一个字符串

    # 用正则表达式去替换内容. re.sub()
    # 结果 = re.sub(正则, 替换之后的结果, 整个字符串)
    # all_content = re.sub(r"<.*?>", "", all_content)
    all_content = content_filter_obj.sub("", all_content)

    print(all_content)
    time.sleep(1)  # 睡眠.安全.
    # break  # 测试
