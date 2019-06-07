from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Count

# Create your views here.


def index(request):
    return render(request,"index.html")


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:

        uphone = request.POST.get("uphone")
        upwd = request.POST.get("upwd")
        user_count = Users.objects.filter(uphone=uphone).aggregate(count=Count("*"))

        if user_count.get("count") == 1:
            user = Users.objects.get(uphone=uphone)
            if upwd == user.upwd:
                return redirect('/')
            else:
                return redirect('/login')
        else:
            return redirect('/login')


def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        dic = {
            "uphone": request.POST.get("uphone"),
            "upwd": request.POST.get("upwd"),
            "uemail": request.POST.get("uemail"),
            "uname": request.POST.get("uname"),
        }
        uphone = request.POST.get("uphone")
        users = Users.objects.filter(uphone=uphone)
        if users:
            errmsg = "手机号已存在"
            return render(request,'register.html',locals())
        else:
            user = Users(**dic)
            user.save()
            return redirect('/')


def cart(request):
    return render(request,"cart.html")



