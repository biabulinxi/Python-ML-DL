# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/9 11:15
# @File_name:02_wtf.py
# @IDE:PyCharm

from flask import Flask, render_template, flash

app = Flask(__name__)

flag = True

app.config["SECRET_KEY"] = "jfiafjfjeaw"

@app.route("/index")
def index():
    global flag
    if flag:
        # 添加闪现信息
        flash("hello1")
        flash("hello2")
        flash("hello3")
        flag = False

    return render_template("index_macro.html")


if __name__ == '__main__':
    app.run(debug=True)














