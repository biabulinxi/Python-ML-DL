# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:19-1-5 下午3:20
# @File_name:hello.py
# @IDE:PyCharm

from flask import Flask, current_app, redirect, url_for

# 创建flask的应用对象
# __name__表示当前的模块名字,
# flask 以此模块目录为总目录，默认static为静态目录，templates为模板目录
app = Flask(__name__)


@app.route("/")
def index():
    """定义的视图函数"""
    return "hello falsk"


# 通过methods限定访问方式
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"

# 一个路径两个视图函数，路径与请求方式一致时，谁在前先访问谁
@app.route('/hello')
def hello():
    return "hello 1"

@app.route('/hello')
def hello2():
    return "hello 2"


# 一个视图函数多个路径
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"


# 一个路径多个视图函数
@app.route('/login')
def login():
    # url = "/"                  # 设置新的路径
    url = url_for("index")       # 通过视图函数反解析路径, 优先使用
    return redirect(url)         # 重定向路径


@app.route('/register')
def register():
    url = "/"
    return redirect(url)


if __name__ == '__main__':
    # 查看整个flask路由信息
    print(app.url_map)
    # 启动flask
    # 设置IP地址和端口
    app.run(debug=True)
