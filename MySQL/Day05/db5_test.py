# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 下午4:31
# @File_name:db5_test.py
# @IDE:PyCharm

from mysqlpython import MysqlPython

#创建对象
sqlh = MysqlPython()
upd = 'update t1 set score=100'
sqlh.exe(upd)

sname = input("请输入查询成绩的名字：")
sele = 'select * from t1 where name=%s'
result = sqlh.refer(sele,[sname])

print('%s的成绩：%s' % (sname,result[0][2]))