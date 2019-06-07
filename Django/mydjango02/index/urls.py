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
from Django.mydjango02.index.views import *

urlpatterns = [
    # 判断请求路径是否为 index
    url(r'^$', index),
    url('login/', login),
    url('register/', register),
    url("01-tmp/",view=temp),
    url("02-tmp/",render_temp),
    url("03-params/",params),
    url('04-static/', static_views),
    url('05-parent/', parent),
    url('06-child/', child),
    url("07-fruit/admin/user/manager/auth/login/", auth, name="auth"),
    url(r"^08-birthday/(\d{4})/(\d{1,2})/(\d{1,2})/$", birthday, name="birth"),

]