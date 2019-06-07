# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午2:27
# @File_name:delete_db.py
# @IDE:PyCharm

import pymongo

conn = pymongo.MongoClient("localhost", 27017)

db_list = conn.database_names()
db_name = "test"

if db_name in db_list:
    mydb = conn[db_name]
    mycol = mydb["acct"]

    # 删除数据
    query = {"acct_no": "6223450000012"}

    ret = mycol.delete_one(query)  # 执行插入
    print("共删除%d条" % ret.deleted_count)

conn.close()
