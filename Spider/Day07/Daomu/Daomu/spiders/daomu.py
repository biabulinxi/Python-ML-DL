# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        # 定义item对象
        item = DaomuItem()
        # 基准xpath,抓取所有章节节点信息
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in articles:
            infoList = article.xpath('./a/text()').extract()[0].split()
            item['bookTitle'] = infoList[0]
            item['zhNum'] = infoList[1]
            item['zhName'] = infoList[2]
            item['zhLink'] = article.xpath('./a/@href').extract()[0]

            yield item
