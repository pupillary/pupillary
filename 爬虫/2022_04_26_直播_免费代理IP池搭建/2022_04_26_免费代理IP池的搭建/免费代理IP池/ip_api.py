# 提供给用户的api接口
from proxy_redis import ProxyRedis

# 提供api接口的模块
# 提供给外界一个http接口. 外界通过访问http://xxxx.xxx.xxxx.xxx:xxxx/get_proxy

from sanic import Sanic, json
from sanic_cors import CORS

# 1.创建app
app = Sanic("ip")  # 随便给个名字
# 2.解决跨域
CORS(app)
red = ProxyRedis()

# 3. 能够处理http请求的函数
@app.route("/get_proxy")
def shenmemingzidoukeyi(req):
    ip = red.get_keyong_proxy()
    return json({"ip": ip})  # 返回给客户端


def run():
    app.run(host="127.0.0.1", port=5800)


if __name__ == '__main__':
    run()
