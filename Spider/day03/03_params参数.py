'''输入搜索内容,获取第2页的响应内容'''
import requests

url = 'http://www.baidu.com/s?'
headers = {'User-Agent':'Mozilla/5.0'}
key = input('输入搜索内容:')
# 定义查询参数(字典)
params = {
        'wd' : key,
        'pn' : '10'
        }
# 发请求,获取响应对象(三步走)
res = requests.get(url,params=params,
                       headers=headers)
res.encoding = 'utf-8'
html = res.text

print(html)










