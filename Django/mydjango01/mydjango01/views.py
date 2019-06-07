# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/18 11:26
# @File_name:views.py
# @IDE:PyCharm


from django.http import HttpResponse


def show(request):
    return HttpResponse("my first django program")


def index(request):
    return HttpResponse("这是我的首页")


def date(request,year,month,day):
    return HttpResponse("生日:%s年%s月%s日" % (year, month, day))
