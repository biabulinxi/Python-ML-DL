# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    bookTitle = scrapy.Field()
    # 章节名称
    zhName = scrapy.Field()
    # 章节数量
    zhNum = scrapy.Field()
    # 章节连接
    zhLink = scrapy.Field()
