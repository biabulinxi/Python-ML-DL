# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 19:27
# @File_name:08_hook.py
# @IDE:PyCharm

from flask import Flask,request,url_for

app = Flask(__name__)


@app.route("/index")
def index():
    print("index 被执行")
    return "index page"


@app.route("/hello")
def hello():
    print("hello 被执行")
    return "hello page"

@app.before_first_request
def handle_before_first_request():
    """在第一次请求之前被执行"""
    print("handle_before_first_request 被执行")


@app.before_request
def handle_before_request():
    """在每次请求之前都被执行, """
    print("handle_before_request 被执行")
    # 返回视图函数完成之后的应答


@app.after_request
def handle_after_request(response):
    """在每次请求（视图函数处理完成之后无异常）之后都被执行, """
    print("handle_after_request 被执行")
    # 返回视图函数完成之后的应答
    return response


@app.teardown_request
def handle_teardown_request(response):
    """在每次请求之后都被执行， 无论视图函数是否有异常，工作在非调试模式时"""
    path = request.path
    if path == url_for("index"):
        print("在请求钩子中判断请求的视图逻辑：index")
    elif path == url_for("hello"):
        print("在请求钩子中判断请求的视图逻辑：hello")

    print("handle_teardown_request 被执行")
    return response



if __name__ == '__main__':
    app.run()