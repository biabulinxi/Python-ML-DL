# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午3:42
# @File_name:acct_manage_svr.py
# @IDE:PyCharm

from socket import *
from typing import Any, Union

import pymongo

host = "127.0.0.1"  # 数据库服务器IP
port = 27017  # 数据库端口
db_name = "test"  # 数据库名称

address = ('0.0.0.0', 9999)  # 服务器绑定地址
db_conn = None  # 数据库连接对象


def conn_database():  # 连接数据库
    global db_conn
    db_conn = pymongo.MongoClient(host, port)
    if not db_conn:
        print("连接数据库失败")
        return -1
    else:
        return 1


def close_database():  # 关闭数据库连接
    if not db_conn:
        return
    else:
        db_conn.close()


def query(msgs):  # 执行查询
    # 获取查询条件
    if msgs[1] == 'all':  # 显示所有
        qry = {}
    else:
        qry = {"acct_no": msgs[1]}
    print(qry)

    # 执行查询
    resp = " "
    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]

        docs = mycol.find(qry) # 执行查询
        for doc in docs:
            acct_info = '帐号:%s,户名：%s,余额：%.2f\n' % \
                        (doc["acct_no"], doc["acct_name"],
                         doc["balance"])
            resp += acct_info  # 每笔数据追加到响应信息后面
    except Exception as e:
        print(e) # 打印错误信息
        print('查询错误')
    return resp  # 返回查询结果


def new_acct(msgs):  # 新增

    acct_no = msgs[1]  # 取帐号
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = msgs[4]

    # 组建字典
    acct_info = {'acct_no': acct_no,
                 "acct_name": acct_name,
                 "acct_type": acct_type,
                 "balance": float(balance)
                 }
    print(acct_info)

    # 执行插入
    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]
        result = mycol.insert_one(acct_info)
        ret = "插入成功,文档ID:%s" % result.inserted_id
    except Exception as e:
        print(e)
        ret = "插入失败"

    return ret


def update_acct(msgs):
    # 获取删除条件
    global rep
    if msgs[1] == 'all':  # 显示所有
        updt = {}
    else:
        updt = {"acct_no": msgs[1]}
    print(updt)

    # 获取修改信息
    update_choose = msgs[2]
    update_infos = msgs[3]
    updt_infos = {"$set":{update_choose:update_infos}}
    # 执行修改
    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]

        result = mycol.update_one(updt,updt_infos,False,False)
        rep = "修改%d笔文档成功" % result.modified_count

    except Exception as e:
        print(e) # 打印错误信息
        print('修改错误')

    return rep  # 返回删除结果


def del_acct(msgs):
    # 获取删除条件
    global rt
    if msgs[1] == 'all':  # 显示所有
        dlt = {}
    else:
        dlt = {"acct_no": msgs[1]}
    print(dlt)

    # 执行删除
    try:
        mydb = db_conn[db_name]
        mycol = mydb["acct"]

        result = mycol.delete_one(dlt) # 执行删除
        rt = "删除%d笔文档成功" % result.deleted_count

    except Exception as e:
        print(e) # 打印错误信息
        print('删除错误')

    return rt  # 返回删除结果


def main():  # 服务器主程序
    # 连接数据库
    global result
    if conn_database() == -1:
        return  # 连接失败，返回
    else:
        conn_database()

    server = socket()  # 创建服务器socket
    server.bind(address)  # 绑定地址
    server.listen(5)  # 监听
    print("服务器已启动")
    sockfd, addr = server.accept()
    while True:
        data = sockfd.recv(2048)  # 接受客户端数据
        if not data:
            print("客户端已关闭")
            break
        # 解析，分发
        print(data.decode())
        msgs = data.decode().split("::")  # 按分隔符拆分返回列表
        if msgs[0] == "query":  # 查询
            result = query(msgs)
        elif msgs[0] == "new":
            result = new_acct(msgs)
        elif msgs[0] == "update":
            result = update_acct(msgs)
        elif msgs[0] == "delete":
            result = del_acct(msgs)
        else:
            print('非法操作请求')
        sockfd.send(result.encode())  # 发送信息至客户端
    close_database()  # 循环退出关闭数据库
    server.close()  # 关闭监听socket


main()
