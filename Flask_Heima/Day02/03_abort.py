# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 14:58
# @File_name:03_abort.py
# @IDE:PyCharm

from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    # name = request.form.get("name")
    # pwd = request.form.grt()
    name = ""
    pwd = ""
    if name != "张三" or pwd != "admin":
        # 使用abort函数可以立即终止视图函数的执行
        # 并返回特定信息到前端
        # 1. 传递状态码信息，必须是标准的http状态码
        abort(404)
        # # 2. 传递响应体信息
        # resp = Response("login filed")
        # abort(resp)

    return "login seccess"


# 定义错误处理的方法
@app.errorhandler(404)
def handle_404_error(err):
    """自定义的错误处理方法"""
    # 这个函数的返回值为前端用户看到的信息
    return "出现了404错误信息，错误信息：%s" % err


if __name__ == '__main__':
    app.run(debug=True)




