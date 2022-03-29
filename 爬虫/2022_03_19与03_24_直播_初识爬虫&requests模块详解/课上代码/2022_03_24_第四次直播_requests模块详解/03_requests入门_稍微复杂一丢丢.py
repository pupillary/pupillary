# 方法论:
# 任何一个网站, 第一件事儿. 观察你要的东西在不在页面源代码
# 如果在
#   直接请求url即可
# 如果不在
#   抓包工具观察. 数据究竟是从哪个url加载进来的

import requests
#
# # 方案一. 不好. 参数太长了.看起来费劲
# # url = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20"
# # headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
# # }
# # resp = requests.get(url, headers=headers)
# # # requests.exceptions.JSONDecodeError: [Errno Expecting value] : 返回的东西不是json字符串
# # # print(resp.text)  # {} []
# # lst = resp.json()
# # print(lst)
#
#
# # 方案二
# url = "https://movie.douban.com/j/chart/top_list"
#
# headers = {
#     # """"Cookie""": """ll="108288"; bid=t2LVfV6dpBk; _vwo_uuid_v2=D95E896F4CF971F7BC8D97A129CF0109F|1fcc2de7f11a8af910fc879a6200e61d; douban-fav-remind=1; __gads=ID=57a791aa157e58ac-22e6c1627dd0003a:T=1644230200:RT=1644230200:S=ALNI_MblChc0hh0gFG47nPRlvJeQ_VCxwg; ct=y; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1648131684%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.775608074.1642491998.1648126288.1648131684.11; __utmb=30149280.0.10.1648131684; __utmz=30149280.1648131684.11.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.712226279.1642492001.1648126316.1648131685.5; __utmb=223695111.0.10.1648131685; __utmz=223695111.1648131685.5.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=e765cc45bb23a73d.1642492001.6.1648132050.1648126332.""",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
# }
# dic = {
#     "type": "13",
#     "interval_id": "100:90",
#     "action": "",
#     "start": "0",  # 0 => 1,  20 => 2  40 => 3
#     "limit": "20",
# }
# # 发送get请求. 并将参数带过去  params传参
# resp = requests.get(url, params=dic, headers=headers)
# print(resp.json())
# print(resp.request.url)

# # 作业上半场
# for i in range(5):
#     start = i * 20  # 0 20 40 60 80
#     url = "https://movie.douban.com/j/chart/top_list"
#
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
#     }
#     dic = {
#         "type": "13",
#         "interval_id": "100:90",
#         "action": "",
#         "start": start,  # 0 => 1,  20 => 2  40 => 3
#         "limit": "20",
#     }
#
#     # 每次循环得到一批新的参数
#     resp = requests.get(url, params=dic, headers=headers)
#     print(resp.json())
#     # 后续工作. 你们来?


# for i in range(5):
#     # url = f"https://www.tupianzj.com/bizhi/DNmeinv/list_77_{i}.html"
#     url = f"https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={i * 20}&limit=20"
#     resp = requests.get(url, headers=None)
#     lst = resp.json()
#     for item in lst:
#         pass
