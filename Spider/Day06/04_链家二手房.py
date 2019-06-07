# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/5 14:48
# @File_name:04_链家二手房.py
# @IDE:PyCharm

import requests
from bs4 import BeautifulSoup
import pymongo

class LianJiaSpider():
    def __init__(self):
        self.baseurl = 'https://bj.lianjia.com/ershoufang/'
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}
        self.conn = pymongo.MongoClient('176.234.100.101',27017)
        self.db = self.conn['lianjiadb']
        self.myset = self.db['houseinfo']

    # 获取页面
    def getPage(self):
        res = requests.get(self.baseurl,headers=self.headers)
        html = res.content.decode('utf-8')
        self.parsePage(html)

    # 解析并保存
    def parsePage(self,html):
        soup = BeautifulSoup(html,'lxml')
        # 获取每个房源的节点
        rList = soup.find_all('li',attrs={'class':'clear LOGCLICKDATA'})
        for r in rList:
            ######################################
            # 查找houseinfo节点
            houseinfo = r.find('div',attrs={'class':'houseInfo'})
            infoList = houseinfo.get_text().split('/')
            name = infoList[0].strip()
            hosenum = infoList[1].strip()
            area = infoList[2].strip()
            #####################################
            # positioninfo节点
            positioninfo = r.find('div',attrs={'class':'positionInfo'})
            pList = positioninfo.get_text().split('/')
            floor = pList[0].strip()
            year = pList[1].strip()
            address = pList[2].strip()
            #####################################
            # 单价和总价
            totalinfo = r.find('div', attrs={'class': 'totalPrice'})
            totalPrice = totalinfo.get_text()
            unitinfo = r.find('div', attrs={'class': 'unitPrice'})
            unitPrice = unitinfo.get_text()
            #####################################
            data = {
                '名称':name,
                '户型':hosenum,
                '面积':area,
                '年份':year,
                '楼层':floor,
                '地点':address,
                '单价':unitPrice,
                '总价':totalPrice,
            }
            print(data)
            self.myset.insert_one(data)

    # 主函数
    def workOn(self):
        self.getPage()


if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.workOn()
