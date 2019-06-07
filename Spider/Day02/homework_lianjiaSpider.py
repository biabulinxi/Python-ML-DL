# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/2 14:00
# @File_name:homework_lianjiaSpider.py
# @IDE:PyCharm


from urllib.request import Request, urlopen
import csv
import re
import pymongo
import pymysql
import time


class LianjiaSpider(object):
    def __init__(self):
        self.baseurl = 'https://xa.fang.lianjia.com/loupan/yanta/pg'
        self.headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}
        # 创建 mongo 连接对象
        self.coon = pymongo.MongoClient('192.168.1.13', 27017)
        self.db = self.coon['lianjia']
        self.myset = self.db['xian']
        # 创建 mysql 连接对象
        self.sqldb = pymysql.connect('192.168.1.13', 'monkey', '123', 'lianjia', charset='utf8')
        self.cursor = self.sqldb.cursor()

    # 获取网页
    def getPages(self, url):
        req = Request(url, headers=self.headers)
        res = urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePages(html)

    # 解析页面
    def parsePages(self, html):
        p = re.compile(
            '<div class="resblock-name">.*?<a.*?>(.*?)</a>.*?<span class="resblock-type".*?>(.*?)</span>.*?<span class="sale-status".*?>(.*?)</span>.*?</div>.*?<div class="resblock-location">.*?<span>(.*?)</span>.*?<a.*?>(.*?)</a>.*?</div>.*?<a class="resblock-room".*?>.*?<span>(.*?)</span>.*?</a>.*?<div class="resblock-area">.*?<span>(.*?)</span>.*?</div>.*?<div class="resblock-price">.*?<div class="main-price">.*?<span class="number">(.*?)</span>.*?<span class="desc">.*?(.*?)</span>.*?<div class="second">(.*?)</div>', re.S)
        rList = p.findall(html)[:-1]
        # print(rList)
        # self.saveCSV(rList)
        self.saveMongodb(rList)
        # self.saveMysql(rList)

    # 保存数据 -- csv
    def saveCSV(self, rList):
        with open('西安链家二手房.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for rt in rList:
                L = [
                    rt[0].strip(),
                    rt[1].strip(),
                    rt[2].strip(),
                    rt[3].strip(),
                    rt[4].strip(),
                    rt[5].strip(),
                    rt[6].strip(),
                    rt[7].strip(),
                    rt[8].strip(),
                    rt[9].strip(),
                ]
                writer.writerow(L)

    # 保存 -- mongodb
    def saveMongodb(self, rList):
        for rt in rList:
            data = {
                '名称': rt[0].strip(),
                '住宅类型': rt[1].strip(),
                '销售状态': rt[2].strip(),
                '地区': rt[3].strip(),
                '地址': rt[4].strip(),
                '几室': rt[5].strip(),
                '面积': rt[6].strip(),
                '均价': rt[7].strip(),
                '单位': rt[8].strip(),
                '总价': rt[9].strip(),
            }
            self.myset.insert_one(data)

    # 保存 -- mysqldb
    def saveMysql(self,rList):
        ins = 'insert into xian values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for rt in rList:
            data = [
                rt[0].strip(),
                rt[1].strip(),
                rt[2].strip(),
                rt[3].strip(),
                rt[4].strip(),
                rt[5].strip(),
                rt[6].strip(),
                rt[7].strip(),
                rt[8].strip(),
                rt[9].strip()
            ]
            self.cursor.execute(ins,data)
            self.sqldb.commit()

    # 主函数
    def workOn(self):
        for pg in range(1,3):
            url = self.baseurl + str(pg)
            self.getPages(url)
            print('第%d页完成' % pg)
            time.sleep(1)
        self.cursor.close()
        self.sqldb.close()


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.workOn()
