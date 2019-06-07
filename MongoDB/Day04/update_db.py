# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午2:13
# @File_name:update_db.py
# @IDE:PyCharm

import pymongo

conn = pymongo.MongoClient("localhost", 27017)

db_list = conn.database_names()
db_name = "test"

if db_name in db_list:
    mydb = conn[db_name]
    mycol = mydb["acct"]

    # 修改数据
    query = {"acct_no":"622345000003"}
    new_value = {"$set":{"balance":99999}}

    ret = mycol.update_one(query,new_value,False,False)  # 执行插入
    print("共修改%d条" % ret.modified_count)

conn.close()
