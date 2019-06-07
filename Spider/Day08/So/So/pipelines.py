# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# 导入scrapy定义好的图片管道类
from scrapy.pipelines.images import ImagesPipeline


# 定义类,继承图片管道类
class SoPipeline(ImagesPipeline):
    # 重写方法
    def get_media_requests(self, item, info):
        # 把图片链接发给调度器
        yield scrapy.Request(item['imgLink'])

