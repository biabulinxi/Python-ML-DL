# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/26 14:29
# @File_name:03_urlencode.py
# @IDE:PyCharm

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote, unquote
from agents import hList
import random
import time


class BaiduSpider(object):
    def __init__(self):
        self.baseurl = 'http://tieba.baidu.com/f?kw='

    # 获取页面
    def getpage(self, url):
        req = Request(url, headers=random.choice(hList))
        res = urlopen(req)
        html = res.read().decode()
        return html

    # 解析页面
    def parsePage(self):
        pass

    # 保存数据
    def writePage(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    # 主函数
    def workOn(self):
        # 对URL编码，拼接URL
        search = input("请输入要搜索的贴吧：")
        key = quote(search)
        url = self.baseurl + key

        for page in range(10):
            pn = (page - 1) * 50
            url += "&pn=" + str(pn)
            # 三步走
            html = self.getpage(url)
            filename = '贴吧_' + search + '_num' + str(page) + 'page.html'
            self.writePage(filename, html)
            print("第%d页保存成功" % page)


if __name__ == '__main__':
    start = time.time()
    spider = BaiduSpider()
    spider.workOn()
    end = time.time()
    print("执行时间：%.2秒" % (end-start))

