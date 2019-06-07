# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/11 10:15
# @File_name:run01.py.py
# @IDE:PyCharm

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-server')
def server01():
    return "这是我的第一个ajax请求"

@app.route('/02-server/<name>')
def server02(name):
    return "欢迎%s" % name

if __name__ == '__main__':
    app.run(debug=True)