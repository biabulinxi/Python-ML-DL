# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/26 17:16
# @File_name:07_有道翻译.py
# @IDE:PyCharm

from urllib.request import Request, urlopen
from urllib.parse import quote, urlencode

# F12 抓取 POST 请求地址
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {"User-Agent": "Mozilla/5.0"}

content = input("请输入要翻译的内容:")

# 1.将数据加载成字典
data = {
    "i":content,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15511718571045",
    "sign":"d04671a5cf956093d507f2a11def3576",
    "ts":"1551171857104",
    "bv":"914275371b3b92d0b61ce3af2c9a3d6f",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false",
}
# 2.进行url编码(字符串)
data = urlencode(data).encode('utf-8')

# 三步走
req = Request(url,data=data,headers=headers)
res = urlopen(req)
html = res.read().decode('utf-8')
print(html)

