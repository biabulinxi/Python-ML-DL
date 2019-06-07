# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 上午9:21
# @File_name:show_dbs.py
# @IDE:PyCharm

import pymongo

# 1.　建立和服务器的连接：MOngoClient
conn = pymongo.MongoClient("localhost", 27017)

# 2. 列出所有库：database_names
db_list = conn.database_names()
if not db_list:
    print("db_list is none!")
else:
    for db in db_list:
        print("db_name:", db)

# 3.　关闭数据库
conn.close()
