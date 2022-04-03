import requests

# url = "https://www.pearvideo.com/videoStatus.jsp?contId=1756814&mrd=0.8773583037760648"

while 1:
    main_url = input("请输入你需要爬取的梨视频的地址: ")  # "https://www.pearvideo.com/video_1756814"

    contId = main_url.split("_")[-1]
    url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"

    headers = {
        "Referer": main_url,  # 处理防盗链
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    dic = resp.json()
    # print(dic)
    src_url = dic['videoInfo']['videos']['srcUrl']
    systemTime = dic["systemTime"]
    src_url = src_url.replace(systemTime, f"cont-{contId}")

    # print(src_url)
    # 下载视频
    print("已经找到视频. 等待下载中....")
    resp = requests.get(src_url, headers=headers)
    with open(f"{contId}.mp4", mode="wb") as f:
        f.write(resp.content)
    print("下载成功")
# 对比
# https://video.pearvideo.com/mp4/third/20220330/cont-1756814-15454898-100434-hd.mp4  # 正常的
# https://video.pearvideo.com/mp4/third/20220330/1648910860599-15454898-100434-hd.mp4  # 破烂
