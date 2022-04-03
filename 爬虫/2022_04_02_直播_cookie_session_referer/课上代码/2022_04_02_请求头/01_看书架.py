import requests

url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"

# 需要带经过验证后的cookie
headers = { #  HOME
    "Cookie": "GUID=67a0291d-d7d5-4d79-81fc-5ea3511a4720; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1646996030,1648554901,1648893030,1648904770; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F19%252F99%252F14%252F95041499.jpg-88x88%253Fv%253D1648893235000%26id%3D95041499%26nickname%3D%25E5%2598%25BB%25E5%2598%25BB%25E5%2598%25BB%25E7%259A%2584%25E6%259D%25B0%25E4%25BC%25A6%26e%3D1664456959%26s%3Dd41e0f61dc503e10; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2295041499%22%2C%22%24device_id%22%3A%2217e6c3e008b1008-0200c415422a4d-f791b31-1638720-17e6c3e008cc0a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2267a0291d-d7d5-4d79-81fc-5ea3511a4720%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1648905001",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
}

resp = requests.get(url, verify=False, headers=headers)
print(resp.text)
resp.json()
