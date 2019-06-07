# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/18 11:45
# @File_name:01_insert.py
# @IDE:PyCharm

import pymysql

# 数据库连接
db = pymysql.connect('localhost', 'root', '123456', 'dict', charset='utf8')

# 创建游标
cursor = db.cursor()
ins = 'insert into words(word, interpretation) values(%s, %s)'

# 打开文件，分行读取并插入数据
with open('dict.txt', 'r') as f:
    # 记录打印的行数
    i = 1
    while True:
        oneLine = f.readline()
        if not oneLine:
            break
        word = oneLine.split()[0]
        interpretation = ' '.join(oneLine.split()[1:])
        # 插入数据库, 用列表传参，补位
        cursor.execute(ins, [word, interpretation])
        # 提交数据库执行
        db.commit()
        print('第%d条存入成功' % i)
        i += 1


cursor.close()
db.close()









