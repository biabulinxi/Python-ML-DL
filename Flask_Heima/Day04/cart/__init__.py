# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 10:34
# @File_name:__init__.py
# @IDE:PyCharm


from flask import Blueprint

app_cart = Blueprint("app_cart", __name__, template_folder="templates")

# 在__init__文件被执行时，把视图加载进来，让蓝图与应用程序知道有视图的存在
from .views import get_cart

