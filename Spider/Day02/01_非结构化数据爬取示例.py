from urllib import request

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1551240859969&di=80124af41e8bd31a882bce1908f2a22c&imgtype=0&src=http%3A%2F%2Fimg3.ph.126.net%2F3FmexX8mjZPfODw2oZ4KMw%3D%3D%2F1352205788134996033.jpg'
headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

# 三步走
req = request.Request(url,headers=headers)
res = request.urlopen(req)
html = res.read()
# 保存
with open('刘德华.jpg','wb') as f:
    f.write(html)















