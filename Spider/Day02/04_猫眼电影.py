# from urllib import request
# import re
# import csv
# import time
#
#
# class Maoyanspider(object):
#     def __init__(self):
#         self.baseurl = 'https://maoyan.com/board/4?offset='
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}
#
#     # 获取页面
#     def getPage(self, url):
#         req = request.Request(url,
#                               headers=self.headers)
#         res = request.urlopen(req)
#         html = res.read().decode('utf-8')
#         self.parsePage(html)
#
#     # 解析页面
#     def parsePage(self, html):
#         # 创建编译对象
#         p = re.compile(
#             '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
#         rList = p.findall(html)
#         print(rList)
#         # rList: [('霸王别姬','张国荣','1993'),(),()]
#         self.writePage(rList)
#
#
#     # 保存页面到csv文件
#     def writePage(self, rList):
#         with open('Film.csv', 'a', newline='') as f:
#             # 创建写入对象
#             writer = csv.writer(f)
#             # ('霸王别姬','张国荣','1993')
#             for rt in rList:
#                 L = [
#                     rt[0].strip(),
#                     rt[1].strip(),
#                     rt[2].strip()
#                 ]
#                 writer.writerow(L)
#
#
#     # 保存页面到本地txt文件
#     def writePage(self, rList):
#         with open('Film.txt', 'a') as f:
#             for rt in rList:
#                 f.write(rt[0].strip() + ' '
#                         + rt[1].strip() + ' '
#                         + rt[2] + '\n')
#
#
#     # 主函数
#     def workOn(self):
#         for pn in range(0, 21, 10):
#             url = self.baseurl + str(pn)
#             print(url)
#             self.getPage(url)
#             time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     spider = Maoyanspider()
#     spider.workOn()


from urllib.request import Request, urlopen
import re
import csv
import time

class MaoyanSpider(object):
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    # 获取页面
    def getPage(self,url):
        req = Request(url,headers=self.headers)
        res = urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)

    # 解析页面
    def parsePage(self,html):
        # 创建编译对象
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rList = p.findall(html)
        self.writePage(rList)

    # 保存页面
    def writePage(self,rList):
        with open('film.csv','a',newline='',encoding='utf-8') as f:
            # 创建写入对象
            writer = csv.writer(f)
            for rt in rList:
                rL = [
                    rt[0].strip(),
                    rt[1].strip(),
                    rt[2].strip(),
                ]
                writer.writerow(rL)

    # 主函数
    def workOn(self):
        for pn in range(0,91,10):
            url = self.baseurl + str(pn)
            self.getPage(url)
            time.sleep(1)


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.workOn()

