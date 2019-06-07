import requests

# 定义常用变量
url = 'http://08imgmini.eastday.com/mobile/20190221/20190221144537_3ed0e29b8624233061e1a36d43f39b5a_1.jpeg'
headers = {'User-Agent':'Mozilla/5.0'}

res = requests.get(url,headers=headers)
html = res.content

with open('赵丽颖.jpg','wb') as f:
    f.write(html)

print('成功') 



















