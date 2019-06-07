# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/9 9:55
# @File_name:02_XSS.py
# @IDE:PyCharm

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/xss", methods=["GET", "POST"])
def xss():
    text = ""
    if request.method == 'POST':
        text = request.form.get("text")

    return render_template("xss.html", text=text)


if __name__ == '__main__':
    app.run(debug=True)
