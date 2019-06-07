from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show01(request):
    return HttpResponse("music 的第一个路由")


def index(request):
    return HttpResponse("这是music的首页")
