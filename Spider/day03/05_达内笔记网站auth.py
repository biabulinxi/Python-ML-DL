import requests
import re
import csv

class Tarenaspider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        # Web客户端认证参数
        self.auth = ('tarenacode','code_2013')
        
    def getPage(self):
        res = requests.get(self.url,
                           headers=self.headers,
                           auth=self.auth,)
        res.encoding = 'utf-8'
        html = res.text
        self.writePage(html)
    
    # 解析和保存数据
    def writePage(self,html):
        p = re.compile('<a href=.*?>(.*?)/</a>',re.S)
        rList = p.findall(html)
        # rList : ['..','AIDCode','']
        with open('Note.csv','w',newline='') as f:
            writer = csv.writer(f)
            for r in rList:
                if r != '..':
                    writer.writerow([r])
        print('写入成功')
        
if __name__ == '__main__':
    spider = Tarenaspider()
    spider.getPage()
