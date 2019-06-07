# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 10:36
# @File_name:views.py
# @IDE:PyCharm


from flask import render_template
from . import app_cart


@app_cart.route("/get_cart")
def get_cart():
    return render_template("cart.html")