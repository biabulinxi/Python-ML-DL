from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("这是index的首页")


def login(request):
    return HttpResponse("这是index登录页面")


def register(request):
    return HttpResponse("这是index注册页面")


def temp(request):
    # 通过loader加载模板
    t = loader.get_template("01-tmp.html")
    # 将模板转换为字符串
    html = t.render()
    # 通过HTTPResponse进行响应
    return HttpResponse(html)


def render_temp(request):
    return render(request, "01-tmp.html")


def params(request):
    name = "张三丰"
    age = 98
    salary = 123.45
    list = ['白眉鹰王',"青翼蝠王"]
    tup = ("赵敏", "周芷若", "小昭")
    dic = {
        "XYJ":"西游记",
        "HLM":"红楼梦",
        "SHZ":"水浒传",
    }
    per = Person()
    per.name = "wangwc"
    per.age = 37
    return render(request,"03-params.html",locals())


class Person(object):
    name = None
    age = None

    def show(self):
        return "姓名:%s，年龄:%s" % (self.name, self.age)


def static_views(request):
    return render(request,"04-static.html")


def parent(request):
    list = ["沙僧","孙悟空","猪八戒","沙僧"]
    return render(request, "05-parent.html", locals())


def child(request):
    list = ["大爸爸", "小爸爸", "猪八戒", "沙僧"]
    return render(request, "06-child.html", locals())

def auth(request):
    return HttpResponse("07-fruit/admin/user/manager/auth/login/")


def birthday(request,year,month,day):
    return HttpResponse("<h1>生日为:%s年%s月%s日</h1>"%(year,month,day))
