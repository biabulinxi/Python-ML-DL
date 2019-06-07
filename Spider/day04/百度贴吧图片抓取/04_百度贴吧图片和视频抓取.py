import requests
from lxml import etree
import time

class Baiduspider(object):
    def __init__(self):
        self.baseurl = 'http://tieba.baidu.com'
        self.url = 'http://tieba.baidu.com/f?'
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    
    # 获取1页中帖子链接
    def getPageUrl(self,params):
        res = requests.get(self.url,
                    params=params,
                    headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        # 从 html 中提取帖子链接
        parseHtml = etree.HTML(html)
        tList = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
#        print(tList)
        # tList : ['/p/2323','/p/2333',...]
        for t in tList:
            tlink = self.baseurl + t
            self.getImgUrl(tlink)
    
    # 获取帖子中图片链接
    def getImgUrl(self,tlink):
        res = requests.get(tlink,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        # 创建解析对象
        parseHtml = etree.HTML(html)
        imgList = parseHtml.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video')
        print(imgList)
        # 遍历每个图片链接
        for img in imgList:
            self.writeImg(img)

    # 保存图片
    def writeImg(self,img):
        res = requests.get(img,
                    headers=self.headers)
        res.encoding = 'utf-8'
        html = res.content
        # 利用字符串切换(后10位)作为文件名
        filename = img[-10:]
        with open('D:\\王伟超\\爬虫\\day04\\百度贴吧图片抓取\\image\\%s' % filename,'wb') as f:
            f.write(html)
        print('%s抓取成功' % filename)
        time.sleep(0.5)
 
    # 主函数
    def workOn(self):
        name = input('贴吧名:')
        start = int(input('起始页:'))
        end = int(input('终止页:'))
        for i in range(start,end+1):
            pn = (i-1)*50
            # 定义查询参数
            params = {
                    'kw' : name,
                    'pn' : str(pn)
                }
            self.getPageUrl(params)
            print('第%d页成功' % i)
    
if __name__ == '__main__':
    spider = Baiduspider()
    spider.workOn()
    
# 错误调试
#1、print测试 ：rList 和 imgList 
#2、空列表 ：
#   1、User-Agent ：IE
#   2、检查xpath表达式
    
    
    
    
    
    
    
    
    