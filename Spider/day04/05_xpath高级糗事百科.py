import requests
import pymongo
from lxml import etree

class Qiushispider(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/text/page/3/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        
    # 获取页面内容
    def getPage(self):
        res = requests.get(self.url,
                    headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html):
        # 创建解析对象
        parseHtml = etree.HTML(html)
        # 每个段子节点对象列表
        baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        # baseList:[element at ...,ele...]
        for base in baseList:
            # 用户昵称
            username = base.xpath('./div/a/h2')
            if username:
                username = username[0].text
            else:
                username = '匿名用户'
            # 段子内容
            content = base.xpath('.//div[@class="content"]/span/text()')[0].strip()
            # 评论数量
            pingNum = base.xpath('.//i[@class="number"]/text()')[0].strip()
            # 好笑数量
            laughNum = base.xpath('.//i[@class="number"]/text()')[1].strip()
            
            d = {
                "username" : username,
                "content"  : content,
                "pingNum"  : pingNum,
                "laughNum" : laughNum
            }
            print(d)
    
    # 保存页面
    def writeMongo(self):
        pass
    
    # 主函数
    def workOn(self):
        self.getPage()
    
if __name__ == '__main__':
    spider = Qiushispider()
    spider.workOn()

















