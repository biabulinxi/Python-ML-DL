import requests

# 测试网址
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
# 普通代理
#proxies = {'http':'http://116.209.58.78:9999'}

# 私密代理
proxies = {'http':'http://309435365:szayclhp@211.149.189.148:16817'}
res = requests.get(url,proxies=proxies,
                       headers=headers)
res.encoding = 'utf-8'
html = res.text

print(html)










