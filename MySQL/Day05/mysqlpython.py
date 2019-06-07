# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 下午3:54
# @File_name:mysqlpython.py
# @IDE:PyCharm

import pymysql

class MysqlPython:
    def __init__(self,host='localhost',user='root',
                 password='123456',database='db5',
                 charset='utf8',port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port

    def open(self):
        self.db = pymysql.connect(host=self.host,user=self.user,
                                  password=self.password,database=self.database
                                  ,charset=self.charset,port=self.port)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def exe(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()
        self.close()

    def refer(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        self.close()
        return result






