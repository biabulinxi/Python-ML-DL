# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/26 11:35
# @File_name:01_urlopen.py
# @IDE:PyCharm

from urllib.request import urlopen, Request


######################################
# 无法设置请求头
url = 'http://www.baidu.com/'
# 向网站发起请求并获取响应对象
response = urlopen(url)
# print(response)
# 获取响应对象的内容
html = response.read().decode('utf-8')
# print(html)


#########################################
# 可以设置请求代理
headers = {'User-Agent':"Mozilla/5.0"}
# 1. 创建请求
request = Request(url, headers=headers)
# 2. 获取响应
response = urlopen(request)
# 3. 获取内容
html = response.read().decode('utf-8')
# print(html)

# 获取 http 响应码
print(response.getcode())
# 返回实际数据的url地址
print(response.geturl())
