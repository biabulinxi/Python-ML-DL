# -*- coding: utf-8 -*-
import scrapy
from CSDN.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    # 允许的域名
    allowed_domains = ['blog.csdn.net']
    # 起始URL地址
    start_urls = ['https://blog.csdn.net/GitChat/article/details/88053194']

    def parse(self, response):
        # 创建item对象
        item= CsdnItem()
        # 提取数据
        item['title'] = response.xpath("//h1[@class='title-article']/text()").extract()[0]
        item['time'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item['number'] = response.xpath('//span[@class="read-count"]/text()').extract()[0]

        yield item
