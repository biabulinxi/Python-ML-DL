# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 18:35
# @File_name:07_session.py
# @IDE:PyCharm

from flask import Flask, session, current_app, g


app = Flask(__name__)

# flask 的session需要用到的秘钥字符串
app.config["SECRET_KEY"] = "bfajdfaankklf4314aejfhuah3849faufa"

# flask 默认把 session 保存到 cookie 中

@app.route("/login", methods=["GET"])
def login():
    # current_app.config

    # 设置session数据
    session["name"] = "python"
    session["mobile"] = "18611111111"
    # g 变量，临时存储的对象变量，每层重启都重置
    g.username = "zhangsan"
    say_hello("zhangsan")
    return "login success"


def say_hello(username):
    username = g.username
    pass


@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)
