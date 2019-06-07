# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 上午11:31
# @File_name:mysql_test.py
# @IDE:PyCharm


import pymysql

# 1. 创建数据库连接对象
db = pymysql.connect("localhost","root","123456",'db5',
                     charset = "utf8")

# 2. 创建游标对象
cur = db.cursor()

# 3. 利用游标对象方法执行sql命令
cur.execute('insert into t1 values(4,"王维",78)')

# 4. 提交到数据库
db.commit()

# 5. 关闭游标对象
cur.close()

# 6. 关闭数据库连接
db.close()

print('存入数据库成功！！！')


