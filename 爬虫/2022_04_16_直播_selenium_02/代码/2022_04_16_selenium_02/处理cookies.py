lst = [{'domain': '.17k.com', 'httpOnly': False, 'name': 'Hm_lpvt_9793f42b498361373512340937deb2a0', 'path': '/', 'secure': False, 'value': '1650121524'}, {'domain': '.17k.com', 'expiry': 1665673523, 'httpOnly': False, 'name': 'accessToken', 'path': '/', 'secure': False, 'value': 'avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F19%252F99%252F14%252F95041499.jpg-88x88%253Fv%253D1648893235000%26id%3D95041499%26nickname%3D%25E5%2598%25BB%25E5%2598%25BB%25E5%2598%25BB%25E7%259A%2584%25E6%259D%25B0%25E4%25BC%25A6%26e%3D1665673523%26s%3De9879e01bb5a181f'}, {'domain': '.17k.com', 'expiry': 1681657524, 'httpOnly': False, 'name': 'Hm_lvt_9793f42b498361373512340937deb2a0', 'path': '/', 'secure': False, 'value': '1650121522'}, {'domain': '.17k.com', 'expiry': 1665673523, 'httpOnly': False, 'name': 'c_csc', 'path': '/', 'secure': False, 'value': 'web'}, {'domain': '.17k.com', 'expiry': 1650124799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.17k.com', 'expiry': 1665673523, 'httpOnly': False, 'name': 'c_channel', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.17k.com', 'expiry': 7957321524, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%2295041499%22%2C%22%24device_id%22%3A%2218032e83c4cab4-0db64eb4b325a8-1734337f-1638720-18032e83c4d12a0%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22a7ac0076-6522-4106-8e79-d127953d23ba%22%7D'}, {'domain': '.17k.com', 'expiry': 1681657521, 'httpOnly': False, 'name': 'GUID', 'path': '/', 'secure': False, 'value': 'a7ac0076-6522-4106-8e79-d127953d23ba'}]
result = {}
for item in lst:  # lst是所有的cookie的信息
    # print(item['name'], item['value'])
    result[item['name']] = item['value']  # 13  # 15
# print(result) #???????? 字典


import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}
# 书架                                                                                                单独给,
resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers=headers, cookies=result)
print(resp.text)
