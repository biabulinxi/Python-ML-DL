# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/4 10:19
# @File_name:01_豆瓣电影.py
# @IDE:PyCharm

from lxml import etree
import requests
import json
import time


class DoubanSpider():
    def __init__(self):
        self.baseurl = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }

    def getpages(self, params):
        res = requests.get(self.baseurl, params=params, headers=self.headers)
        html = res.content.decode('utf-8')
        self.parsepages(html)

    def parsepages(self, html):
        # 把json的字符串html，转回python
        fList = json.loads(html)
        for f in fList:
            name = f['title']
            score = f['score']
            r = name + score + '\n'
            self.writepages(r)

    def writepages(self, r):
        with open('豆瓣.csv', 'a', encoding='utf-8',newline='') as f:
            f.write(r)
            time.sleep(0.5)

    def workon(self):
        type = input('请输入查看的电影类型(剧情，喜剧，爱情):')
        num = int(input('请输入需要抓取的电影数量:'))
        params = {
            'type': type,
            'interval_id': '100:90',
            'action': '',
            'start': '0',
            'limit': num,
        }
        self.getpages(params)
        print('%d已爬取' % num)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.workon()
