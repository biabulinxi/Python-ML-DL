"""mydjango01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # 访问路径 show/ ，视图views.show()
    # url('show/', show),
    path('show/', show), # 同样可以完成
    # 访问主页127.0.0.1:8000，index
    # url(r"^$", index)

    # 带参数的路由, 输出生日
    url(r"^date/(\d{4})/(\d{1,2})/(\d{1,2})/$", date),

    # 配置分布式 music 路由，判断访问路径是否为 music/ 开头
    url(r"^music/", include("music.urls")),
    url("", include("index.urls")),
    url(r"^sport/", include("sport.urls")),
    url(r"^news/", include("news.urls")),

]
