# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 17:26
# @File_name:06_cookin.py
# @IDE:PyCharm

from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set_cookie", methods=["GET"])
def index():
    resp = make_response("success")
    # 设置cookie, 默认有效期是临时cookie，浏览器关闭时就销毁
    resp.set_cookie("itcast","python")
    resp.set_cookie("itcast1","python1")
    # max-age 设置有效期，单位秒
    resp.set_cookie("itcast2","python2",max_age=3600)
    resp.headers["Set-Cookie"] = "itcast3=python3; " \
                                 "Expires=Tue, 08-Jan-2019 " \
                                 "10:59:19 GMT; Max-Age=3600; Path=/"
    return resp


@app.route("/get_cookie")
def get_cookin():
    c = request.cookies.get("itcast")
    return c


@app.route("/delete_cookie")
def delete_cookin():
    resp = make_response("del success")
    # 删除cookie
    resp.delete_cookie("itcast2")
    return resp


if __name__ == '__main__':
    app.run(debug=True)