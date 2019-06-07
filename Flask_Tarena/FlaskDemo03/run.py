# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/24 10:22
# @File_name:run.py
# @IDE:PyCharm

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/01_parent")
def parent():
    return render_template("01_parent.html")


@app.route('/02_child')
def child():
    return render_template("02_child.html")


# 127.0.0.1:5000/03_resquest
@app.route("/03_request")
def request_views():
    # print(dir(request))
    scheme = request.scheme        # 协议
    method = request.method        # 请求方式
    args = request.args            # get 请求数据
    form = request.form            # post 请求数据
    cookies = request.cookies      # cookies
    files = request.files          # 上传文件
    path = request.path            # 请求资源路径（不含参数）
    full_path = request.full_path  # 请求资源路径
    url = request.url              # 完整路径
    headers = request.headers      # 请求消息头

    return render_template("03_request.html", params = locals())


# Referer 请求原地址
@app.route("/04_referer")
def rederer_views():
    return redirect(url_for('request_views'))


if __name__ == '__main__':
    app.run(debug=True)












