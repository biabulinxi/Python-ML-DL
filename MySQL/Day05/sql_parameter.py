# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 下午3:34
# @File_name:sql_parameter.py
# @IDE:PyCharm

'''SQL语句命令参数化'''

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root',password = '123456',
                     database = 'db5',charset = 'utf8')
cus = db.cursor()

#用户输入
sid = input('请输入id:')
sname = input('请输入name:')
sscore = input('请输入score:')

ins = 'insert into t1 values(%s,%s,%s)'
param = [sid,sname,sscore]
# 定义sql变量
try:
    # 必须用列表进行传参
    cus.execute(ins,param)

    db.commit()
    print("OK")
except Exception as e:
    db.rollback()
    print("failed",e)

cus.close()
db.close()

