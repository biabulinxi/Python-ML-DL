"""
小米应用商店的社交软件抓取
"""

import requests
from multiprocessing import Queue
from threading import Thread
import time
import json
import urllib.parse


class XiaomiSpider():
    def __init__(self):
        self.baseurl = 'http://app.mi.com/categotyAllListApi?'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()

    # url队列
    def getUrl(self):
        # 20个URL地址，放到队列中
        for page in range(50):
            params = {
                'page':str(page),
                'categoryId': '2',
                'pageSize': '30',
            }
            # 对params进行编码
            params = urllib.parse.urlencode(params)
            # 获取完整URL
            url = self.baseurl + params
            self.urlQueue.put(url)

    # 解析队列
    def getHtml(self):
        while True:
            if self.urlQueue.empty():
                break
            else:
                url = self.urlQueue.get()
                res = requests.get(url,headers=self.headers)
                html = res.content.decode('utf-8')
                self.parseQueue.put(html)

    # get获取HTML，提取保存数据
    def parseHtml(self):
        while True:
            try:
                # json 字符串
                html = self.parseQueue.get(block=True,timeout=0.5)
                dList = json.loads(html)['data']
                baselink = 'http://app.mi.com/details?id='
                for data in dList:
                    d = {
                        'name':data['displayName'],
                        'link':baselink + data['packageName']
                    }
                    with open('app.json','a',encoding='utf-8') as f:
                        f.write(str(d)+'\n')
            except:
                break

    # 主函数
    def workOn(self):
        # URL队列
        self.getUrl()
        # 创建采集线程
        thread=[]
        for i in range(5):
            t = Thread(target=self.getHtml())
            thread.append(t)
            t.start()
        # 创建解析线程
        for i in range(5):
            t = Thread(target=self.parseHtml())
            thread.append(t)
            t.start()
        # 回收线程
        for t in thread:
            t.join()


if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print('执行时间：%.2f' % (end - start))
