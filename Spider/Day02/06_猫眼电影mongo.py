from urllib import request
import re 
import time 
import pymongo

class Maoyanspider(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}
        self.page = 1
        # 创建三个对象
        self.conn = pymongo.MongoClient(
                      '192.168.1.13',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['film']
    
    # 获取页面
    def getPage(self,url):
        req = request.Request(url,
                    headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html):
        # 创建编译对象
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rList = p.findall(html)
        # rList: [('霸王别姬','张国荣','1993'),(),()]
        self.writeMongo(rList)

    # 保存页面到mongdb数据库
    def writeMongo(self,rList):
        for rt in rList:
            d = {
                 'name' : rt[0].strip(),
                 'star' : rt[1].strip(),
                 'releasetime' : rt[2].strip()
                }
            self.myset.insert_one(d)
        
    # 主函数
    def workOn(self):
        for pn in range(0,21,10):
            url = self.baseurl + str(pn)
            self.getPage(url)
            print('第%d页完成' % self.page)
            self.page += 1
            time.sleep(0.5)
    
if __name__ == '__main__':
    spider = Maoyanspider()
    spider.workOn()














