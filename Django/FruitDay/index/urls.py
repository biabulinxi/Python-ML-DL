# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/19 9:39
# @File_name:urls.py
# @IDE:PyCharm

"""
index的路由
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    # 判断请求路径是否为 index
    url(r'^$', index),
    url('login/', login),
    url('register/', register),
    url('cart/', cart),

]