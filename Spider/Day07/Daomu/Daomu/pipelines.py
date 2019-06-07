# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from Daomu.settings import *
import pymysql


class DaomuPipeline(object):
    def process_item(self, item, spider):
        print('*' * 50)
        print(item['bookTitle'])
        print(item['zhName'])
        print(item['zhNum'])
        print(item['zhLink'])
        print('*' * 50)
        return item


# 存入mongodb数据库管道
class DaomuMongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        # 把item对象转为字典
        bookInfo = dict(item)
        self.myset.insert_one(bookInfo)
        return item


class DaomuMysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        # 把item对象转为字典
        bookInfo = dict(item)
        self.cursor.insert_one(bookInfo)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print('我是close_spider')
