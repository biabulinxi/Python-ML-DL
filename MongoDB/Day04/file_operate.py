# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午2:44
# @File_name:file_operate.py
# @IDE:PyCharm

from pymongo import MongoClient
import bson.binary

from_img = "th.jpg"
to_img = "test_new.jpg"

conn = MongoClient("localhost",27017)
db = conn.gridfs  # 获取库对象
mycol = db.image  # 获取集合对象


def save_img(mycol): # 存文件
    f = open(from_img, 'rb')  # 二进制读取
    data = f.read()  # 读取文件内容
    content = bson.binary.Binary(data)  # 格式转换
    mycol.insert({"filename":from_img, "data": content})
    f.close()
    print("save ok")
    return

def get_img(mycol): # 从数据库读取文件
    img = mycol.find_one({"filename":from_img})
    with open(to_img, 'wb') as f:
        f.write(img["data"])

    print("save new file ok")


# save_img(mycol)
get_img(mycol)

conn.close()

