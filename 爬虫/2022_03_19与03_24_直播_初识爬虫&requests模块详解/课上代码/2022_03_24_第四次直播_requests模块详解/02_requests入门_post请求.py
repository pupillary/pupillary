import requests

url = "https://fanyi.baidu.com/sug"  # 抓包里看到的

# 准备参数
data = {
    "kw": "jay"   # 抓包里看到的
}
# Form Data => data
resp = requests.post(url, data=data)  # post 抓包里看到的
# print(resp.text)  # 这里返回的是一个json字符串
# import json
# dic = json.loads(resp.text)
# print(dic)  # 这是方案一

# # 前提. 服务器返回的必须是json字符串才可以.
# # print(resp.text)  # 建议在这里来确定是否是json
# dic = resp.json()  # 这里是方案二, 能直接把返回的内容处理成json
#
# print(dic)

# resp.text  # 单纯, 拿文本. html, json  => 字符串
# resp.json()  #  不单纯, 只能拿json => 字典


