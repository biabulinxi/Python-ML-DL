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
    url("01-add/",add_views),
    url("02-query",query_views),
    url("03-query-filter", query_filter),
    url("04-update",update_views),
    url("05-delete",delete_query),
    url(r"^06-delete/(\d+)/$",delete),
]

urlpatterns += [
    url('07-oto/',oto_views),
    url("10-request",request_views),
    url("11-get",get_views),
    url("12-post", post_views),
    url('13-form/',form_views),
    url('13-register/', register_views),
    url('15-modelform', modelform_views),
    url('16-widget1', widget1_views),
]

urlpatterns += [
    url('17-setcookie/',setcookie),
    url('18-getcookie/',getcookie),
    url('19-setsession/',setsession),
    url('20-getsession/',getsession),
]