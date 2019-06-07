# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 下午2:45
# @File_name:fatch.py
# @IDE:PyCharm

import pymysql

db = pymysql.connect('localhost','root','123456',charset = 'utf8')

cur = db.cursor()
try:
    cur.execute('use db5')
    cur.execute('select * from t1')
    fetchone = cur.fetchone()
    print(fetchone)
    fetchmany = cur.fetchmany(2)
    print("-------------------------------")
    print(fetchmany)
    fetchall = cur.fetchall()
    print("-------------------------------")
    print(fetchall)
except:
    print('查询失败！！！')

cur.close()
db.close()

print('查询成功！！！')