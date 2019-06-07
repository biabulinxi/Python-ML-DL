# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 16:09
# @File_name:04_respose.py
# @IDE:PyCharm

# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 14:58
# @File_name:03_abort.py
# @IDE:PyCharm

from flask import Flask, request, abort, Response, make_response

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    # 1. 使用元祖，返回自定义的相应信息
    #         响应体      响应码(可自定义)               响应头
    # return "index page", 400, [("Itcast","python"), ("City", "shenzhen")]
    # return "index page", 400, {"Itcast":"python", "City":"shenzhen"}
    # return "index page", 666, {"Itcast":"python", "City":"shenzhen"}
    # return "index page", "666", {"Itcast": "python", "City": "shenzhen"}

    # 2. 使用make_response 来构造响应信息
    resp = make_response("index page 2")
    resp.status = "999 itcast"   # 设置状态码
    resp.headers["city"] = "sz"  # 设置响应头
    return resp


if __name__ == '__main__':
    app.run(debug=True)
