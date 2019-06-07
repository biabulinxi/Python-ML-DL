# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 上午11:13
# @File_name:insert_db.py
# @IDE:PyCharm

import pymongo

conn = pymongo.MongoClient("localhost", 27017)

db_list = conn.database_names()
db_name = "test"

if db_name in db_list:
    mydb = conn[db_name]
    mycol = mydb["acct"]

    # 插入的数据
    my_dict = {
        "acct_no": "6223450000010",
        "acct_name": "Tom",
        "balance": 45678
    }

    ret = mycol.insert(my_dict)  # 执行插入
    print("NewID:",ret.inserted_id)

conn.close()