# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 下午2:13
# @File_name:add_del_alter.py
# @IDE:PyCharm

'''在db5库中添加修改删除一条记录'''

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root',password = '123456',
                     database = 'db5',charset = 'utf8')
cus = db.cursor()
try:
    cus.execute('insert into t1 values(5,"taoyuanming",85)')
    cus.execute('update t1 set score=100 where name = "dufu"')
    cus.execute('delete from t1 where name = "libai"')
    db.commit()
    print("删除数据成功！！！")
except:
    db.rollback()
    print("删除数据失败！！！")

cus.close()
db.close()

