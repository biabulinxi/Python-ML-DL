# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 上午10:56
# @File_name:sort_db.py
# @IDE:PyCharm

import pymongo

conn = pymongo.MongoClient("localhost",27017)
db_list = conn.database_names()
db_name = 'test'
if db_name in db_list:
    mydb = conn[db_name]  # 获取库
    mycol = mydb["acct"]  # 获取集合

    docs = mycol.find({})
    sorted_docs = docs.sort([("balance", pymongo.ASCENDING)])  # !!!

    for doc in sorted_docs:
        acct_info = "帐号:%s, 户名:%s, 余额:%f" % \
                    (doc["acct_no"], doc["acct_name"], doc["balance"])
        print(acct_info)

conn.close()
