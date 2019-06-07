# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 上午11:38
# @File_name:insert_many.py
# @IDE:PyCharm


import pymongo

conn = pymongo.MongoClient("localhost", 27017)

db_list = conn.database_names()
db_name = "test"

if db_name in db_list:
    mydb = conn[db_name]
    mycol = mydb["acct"]

    # 插入的数据
    my_dict = [
        {
            "acct_no": "6223450000011",
            "acct_name": "二哈",
            "balance": 99999
        },
        {
            "acct_no": "6223450000012",
            "acct_name": "邓鹏",
            "balance": 88888
        }
    ]

    ret = mycol.insert_many(my_dict)  # 执行插入
    print("NewID:", ret.inserted_ids)

conn.close()
