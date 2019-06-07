# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from ..items import SoItem
import json


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    baseurl = 'http://image.so.com/zj?'
    # start_urls = ['http://image.so.com/']

    def start_requests(self):
        # 拼接url地址，发给调度器
        for page in range(3):
            params = {
                'ch': 'beauty',  # 图片分类
                'sn': str(page*30),  # sn表示图片编号,0(1-30张),30(31-60张)
                'listtype': 'new',
                'temp': '1',
            }
            # 返回json的url
            url = self.baseurl + parse.urlencode(params)
            yield scrapy.Request(url, callback=self.parseImg)

    def parseImg(self, response):
        # 创建item对象
        item = SoItem()
        # 提取连接
        html = response.text
        html = json.loads(html)
        for img in html['list']:
            item['imgLink'] = img['qhimg_url']
            yield item
