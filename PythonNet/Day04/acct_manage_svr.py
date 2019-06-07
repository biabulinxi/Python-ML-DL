# @Project:AID1810
# @Author:biabu
# @Date:18-12-11 下午4:19
# @File_name:acct_manage_svr.py
# @IDE:PyCharm

from socket import *
import pymysql

host = "127.0.0.1"  # 数据库服务器IP
user = "root"  # 用户名
passwd = '123456'  # 用户密码
name = "test"  # 数据库名称
address = ('0.0.0.0', 9999)  # 服务器绑定地址
conn = None  # 数据库连接对象


def conn_database():  # 连接数据库
    global db_conn
    db_conn = pymysql.connect(host, user, passwd, name)
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
    global db_conn
    cursor = db_conn.cursor()
    if msgs[1] == 'all':  # 显示所有
        sql = "select * from acct"
    else:
        sql = "select * from acct "
        sql += "where acct_no = '%s' " % msgs[1]
    print(sql)
    resp = ''  # 查询响应字符串
    try:
        cursor.execute(sql)
        result = cursor.fetchall()  # type: object # 获取所有
        for row in result:
            acct_no = row[0]  # 账户
            acct_name = row[1]  # 用户名
            balance = row[4]  # 余额
            acct_info = '帐号:%s,户名：%s,余额：%.2f\n' % \
                        (acct_no, acct_name, balance)
            resp += acct_info  # 每笔数据追加到响应信息后面
    except:
        print('查询错误')
    return resp  # 返回查询结果


def new_acct(msgs):  # 新增
    result = 0
    global db_conn
    cursor = db_conn.cursor()  # 获取游标
    acct_no = msgs[1]  # 取帐号
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = msgs[4]
    # insert into acct
    # values()
    sql = '''insert into acct values('%s','%s',now(),%s,%s)''' % \
          (acct_no,acct_name,acct_type,balance)
    print(sql)
    try:
        result = cursor.execute(sql)
        db_conn.commit()  # 提交事物
    except:
        db_conn.rollback()
    ret = '操作结果影响%d行' % result
    return ret


def main():  # 服务器主程序
    # 连接数据库
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
            pass
        elif msgs[0] == "delete":
            pass
        else:
            print('非法操作请求')
        sockfd.send(result.encode())  # 发送信息至客户端
    close_database()  # 循环退出关闭数据库
    server.close()  # 关闭监听socket


main()
