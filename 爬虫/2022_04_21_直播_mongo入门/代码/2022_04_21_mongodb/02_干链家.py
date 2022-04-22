import requests
from lxml import etree
import pymongo
import pymysql


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}


def get_page_source(url):  # 获取页面源代码
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_data(pgsource):  # 解析页面源代码. 获取到数据
    tree = etree.HTML(pgsource)
    li_list = tree.xpath("//*[@class='sellListContent']/li")

    # print(len(li_list))
    result = []
    for li in li_list:
        title = li.xpath(".//*[@class='title']/a/text()")
        if not title:  # 如果title没东西. 再见
            continue
        title = title[0]  # 根据你的实际情况.取[0] 或者用join()处理
        postion = li.xpath(".//*[@class='positionInfo']//text()")
        postion = "".join(postion).strip().replace(" ", "")

        house_infos = li.xpath(".//*[@class='houseInfo']//text()")
        infos = house_infos[0].replace(" ", "").split("|")
        # print(infos)  # 不再处理了

        totle = li.xpath(".//*[@class='priceInfo']/div[1]//text()")
        price = li.xpath(".//*[@class='priceInfo']/div[2]//text()")
        totle = "".join(totle)
        price = price[0]
        dic = {
            "title": title,
            "price": price,
            "totle": totle,
            "postion": postion,
            "infos": infos,
        }
        result.append(dic)
    return result


def save_mongo(data):
    conn = pymongo.MongoClient(host="localhost", port=27017)
    db = conn['cool']
    db.yunsir.insert_many(data)  # 自己选择
    conn.close()


def save_mysql(data):
    pass  # 测试的时候不要加try...except...  redis


def save_data(data):
    save_mongo(data)
    save_mysql(data)


def main():
    url = "https://bj.lianjia.com/ershoufang/"
    page_source = get_page_source(url)
    data = parse_data(page_source)
    save_data(data)


if __name__ == '__main__':
    main()
