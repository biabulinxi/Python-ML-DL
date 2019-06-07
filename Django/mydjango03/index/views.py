from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Avg, Sum, Count
from .forms import *


# Create your views here.

def add_views(request):
    # 向author中添加信息数据
    # 方式一：Entry.objects.create()
    # author = Author.objects.create(name="水域请", age=86, email="laoshe@163.com")

    # 方式二：创建实体对象，并调用save()方法
    # author = Author()
    # author.name = "巴金"
    # author.age = 76
    # author.email = "bajin@163.com"
    # author.save()

    # 方式三：
    # dic = {
    #     "name": "鲁迅",
    #     "age": 76,
    #     "email": "luxun@163.com",
    # }
    # author = Author(**dic)
    # author.save()

    # 向Book插入数据
    # book = Book.objects.create(title="三味书屋",publicate_date="1896-9-10")
    # book = Book()
    # book.title = "蛋蛋"
    # book.publicate_date = "2018-10-2"
    # book.save()
    # dic = {
    #     "title":"百草园",
    #     "publicate_date":"1988-10-15"
    # }
    # book=Book(**dic)
    # book.save()

    # publisher
    publisher = Publisher.objects.create(name="星球", address="雁塔", city="西安", country="中国", webdite="http://1234.com")

    # publisher = Publisher()
    # publisher.name = "火星"
    # publisher.address = "曲江"
    # publisher.city = "西安"
    # publisher.country = "中国"
    # publisher.webdite = "http://123.com"
    # publisher.save()
    #
    # dic1 = {
    #     #     "name": "地球",
    #     #     "address": "未央",
    #     #     "city": "西安",
    #     #     "country": "中国",
    #     #     "webdite": "http://12.com",
    #     # }
    #     # publisher = Publisher(**dic1)
    #     # publisher.save()

    return HttpResponse("Create Success！！！")


def query_views(request):
    # all() 查询实体中所有的数据
    authors = Author.objects.all()
    # authors 是一个可迭代对象
    for au in authors:
        print("ID%s,姓名：%s,年龄:%d,邮箱:%s" % (au.id, au.name, au.age, au.email))
    return HttpResponse("query ok")


def query_filter(request):
    # 1. 查询author实体中id为1的信息
    authors = Author.objects.filter(id=1)
    print(authors)
    # 2. 查询author实体中id为1的并且在isActive为True
    authors = Author.objects.filter(id=1, isActive=True)
    print(authors.query)

    # 3.查询auther中的age大于巴金age的信息
    authors = Author.objects.filter(
        age__gt=(
            Author.objects.filter(
                name="巴金"
            ).values('age')
        )
    )

    print("sql:", authors.query)
    for au in authors:
        print(au.name, au.age)

    # 查询返回第一条数据
    authors = Author.objects.get(id=1)

    # 聚合查询
    result = Author.objects.aggregate(
        avgAge=Avg('age'), sumAge=Sum("age")
    )
    print(result)

    # 查询author中 age>80 的人的平均年龄
    result = Author.objects.filter(age__gte=80).aggregate(avg=Avg('age'))
    print(result)

    # 按照 isActive 进行分组，求每组人数
    result = Author.objects.values("isActive").annotate(count=Count("*")).values("isActive", "count")
    print("按照 isActive 进行分组，求每组人数\n", result)

    # 1.查询 Book 表中共有本图书
    sum_book = Book.objects.aggregate(count=Count(id))
    print("Book 表中共有本图书", sum_book)

    # 2.查询 每个时间 所发布的书籍的数量
    num_book = Book.objects.values("publicate_date").annotate(count=Count("*"))
    print("每个时间 所发布的书籍的数量", num_book)
    # 3.查询 1980 年之后所出版的图书数量
    bks = Book.objects.filter(publicate_date__year__gte=1980).aggregate(count=Count('*'))
    print("1980 年之后所出版的图书数量", bks)

    # 4.查询 Publisher中，City为西安的出版社数量
    pblsnum = Publisher.objects.filter(city='西安').aggregate(count=Count('*'))
    print("Publisher中，City为西安的出版社数量", pblsnum)

    return HttpResponse("query ok")


def update_views(request):
    # 将老舍的邮箱 更改为 laoshe@sina.com
    # au = Author.objects.get(name="老舍")
    # au.email = "laoshe@sina.com"
    # au.save()

    # 将 isActive 为0的全部修改成 1
    # Author.objects.filter(isActive=False).update(isActive=True)
    # 更新Author表中所有的数据的age都加10岁
    from django.db.models import F, Q
    Author.objects.all().update(age=F('age') + 10)

    # 查询Author表中id = 1或age >= 90的人的信息
    Author.objects.filter(Q(id=1) | Q(age__gte=90))

    return HttpResponse("修改成功！！！")


def delete_query(request):
    authors = Author.objects.filter(isActive=True)
    return render(request, "06-delete.html", locals())


def delete(request, id):
    Author.objects.filter(id=id).update(isActive=False)
    return redirect('/05-delete')


def oto_views(request):
    # 查询舒服人对应的 author 信息
    wife = Wife.objects.get(name="舒夫人")
    print("夫人姓名：%s,年龄%s" % (wife.name, wife.age))
    author = wife.author
    print("作者姓名:", author.name)
    # 查询老舍对应的wife信息
    author = Author.objects.get(name="巴金")
    print(author.name, author.wife.name)

    # 查询book 的 出版社
    book = Book.objects.get(title="蛋蛋")
    print("蛋蛋的出版社是", book.publisher)

    # 查 出版社 对应的 书籍
    pub = Publisher.objects.get(name="地球")
    books = pub.book_set.all()
    print("地球出版社,出版的书籍:")
    for bk in books:
        print("书名:%s" % bk.title)

    return HttpResponse("query ok")


def request_views(request):
    print("request：",request)
    print("request成员：")
    print(dir(request))
    return HttpResponse("Request OK")


def get_views(request):
    pname = request.GET.get("pname","")
    return HttpResponse("您搜索的产品名称为:"+pname)


def post_views(request):
    # 判断请求方式，get去往12-post.html，post接收请求提交的数据
    if request.method == "GET":
        return render(request, "12-post.html")
    else:
        uname = request.POST.get("uname","unknown")
        return HttpResponse("用户名称："+uname)


def form_views(requesst):
    form = RemarkForm()
    return render(requesst,'13-form.html',locals())


def register_views(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,'13-register.html', locals())
    else:
        ############################
        # 标准取值
        # uname = request.POST.get("uname", "unknown")
        # upwd = request.POST.get("upwd", "unknown")
        # uage = request.POST.get("uage", "unknown")
        # uemail = request.POST.get("uemail", "unknown")
        # return HttpResponse("注册成功!\n用户名:%s,用户密码:%s,年龄:%s,邮箱:%s" % (uname, upwd, uage,uemail))

        ##################################
        # 通过Form取值
        # 1. 将request.post提交给表单类
        form = RegisterForm(request.POST)
        # 2. 进行数据验证是否有效
        if form.is_valid():
            # 3. 通过验证取值
            data = form.cleaned_data
            print(data)
            return HttpResponse("取值成功")


def modelform_views(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, '15-modelform.html',locals())
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author(**data).save()
            return HttpResponse("保存数据成功")

def widget1_views(request):
    if request.method == "GET":
        form = WidgetModelForm()
        return render(request,'16-widget1.html',locals())


def setcookie(request):
    resp = HttpResponse('添加cookie成功')
    resp.set_cookie('uphone','13912345678',60*60*24*365*10)
    return resp

def getcookie(request):
    uphone = request.COOKIES.get('uphone','None')
    return HttpResponse("cookie的值为"+uphone)

def setsession(request):
    request.session['uphone'] = '13912345678'
    return HttpResponse("添加session成功")

def getsession(request):
    uphone = request.session['uphone']
    return HttpResponse('uphone:'+uphone)
