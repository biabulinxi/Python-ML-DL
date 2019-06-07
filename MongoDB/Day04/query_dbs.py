# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 上午9:40
# @File_name:query_dbs.py
# @IDE:PyCharm

import pymongo

# 建立连接
conn = pymongo.MongoClient("localhost", 27017)
# conn = pymongo.MongoClient("Mongodb://localhost:27017")

# 获取数据库对象
dblist = conn.database_names()
dbname = "test"
if dbname in dblist:
    mydb = conn["test"]  # use test
    mycol = mydb["acct"] # 获取集合对象
    # query = {} # 不带筛选查询
    # query = {"acct_name":"Jerry"} # 带筛选查询
    # query = {"balance":{"$gte":5000}} # 带筛选查询
    query = {"$or":[{"acct_name":"Jerry"},{"acct_name":"Rose"}]} # 带筛选查询
    # project = {"id":0} # 不显示id域
    project = {"_id":False}
    docs = mycol.find(query,project) # 执行查询
    # 取指定域打印
    for doc in docs:
        acct_info = "帐号:%s, 户名:%s, 余额:%f" % \
                    (doc["acct_no"],doc["acct_name"],doc["balance"])
        print(acct_info)

# 关闭连接
conn.close()




