import requests

# 定义常用变量
url = 'http://www.baidu.com/'
headers = {'User-Agent':'Mozilla/5.0'}
# 向网站发请求并获取响应对象
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
# 获取字符串
html = res.text
# 获取bytes类型
html = res.content
# 获取http响应码
print(res.status_code)
# 获取返回实际数据URL
print(res.url)
















