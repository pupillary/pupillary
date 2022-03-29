import requests

url = "https://desk-fd.zol-img.com.cn/t_s960x600c5/g5/M00/00/07/ChMkJl3qNKaIDNA2AARqqK0FxbEAAvnJAJbLQMABGrA592.jpg"

resp = requests.get(url)
# print(resp.text)  # 你访问的url并不是一个文本
content = resp.content  # 拿到的是字节

# 存起来?
with open("哈哈.jpg", mode="wb") as f:
    f.write(content)
