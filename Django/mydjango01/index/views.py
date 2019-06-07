from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("这是index的首页")


def login(request):
    return HttpResponse("这是登录页面")


def register(request):
    return HttpResponse("这是注册页面")
