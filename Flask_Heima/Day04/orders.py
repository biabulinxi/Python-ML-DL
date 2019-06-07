# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 10:21
# @File_name:orders.py
# @IDE:PyCharm

from flask import Blueprint


# 创建蓝图对象，蓝图就是一个小模块概念
app_orders = Blueprint("app_orders", __name__)


# 创建蓝图路由
@app_orders.route('/get_order')
def get_order():
    return "get orders page"


