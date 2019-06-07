# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/26 14:29
# @File_name:03_urlencode.py
# @IDE:PyCharm

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote, unquote

# 定义常用的变量
headers= {"User-Agent":'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)'}
baseurl = "http://tieba.baidu.com/f?kw="
# 对URL编码，拼接URL
search = input("请输入要搜索的贴吧：")
key = quote(search)
url = baseurl + key

for page in range(10):
    pn = (page - 1) * 50
    url += "&pn=" + str(pn)
    # 三步走
    req = Request(url,headers=headers)
    res = urlopen(req)
    html = res.read().decode('utf-8')

    # 保存到文件
    with open('贴吧_'+search+'_num'+str(page)+'page.html','w',encoding='utf-8') as f:
        f.write(html)
print("保存成功")