# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午3:41
# @File_name:acct_manage_cli.py
# @IDE:PyCharm


"""
数据格式
    查询：
        请求：
            query::all              # 查询所有账户
            query::622345000001　　　# 查询指定账户
        相应：
            账号：622345000001,户名：Jerry,余额：1000
    新增：
        请求：
            new:622345000002::Tom::1::10.00
        响应：
            执行一笔操作
"""

from socket import *

client = None  # 客户端socket
host = "127.0.0.1"
port = 9999


# 打印菜单
def print_menu():
    menu = '''
    ------------------账户管理系统----------------------
        1 - 查询账户
        2 - 新建账户
        3 - 修改账户
        4 - 删除账户
        5 - 退出
    '''
    print(menu)


def open_coon():  # 连接后台服务器
    try:
        global client
        client = socket()  # 创建socket
        client.connect((host, port))
        print('连接服务器成功')
        return 0
    except:
        print('连接服务器失败')
        return -1


def send_msg(msg):  # 向服务器端发送信息
    if not client:  # socket 没有被创建
        return -1
    n = client.send(msg.encode())  # 调用socket发送
    return n


def recv_msg():  # 接收服务器相应
    if not client:
        return None
    data = client.recv(2048)  # 调用socket接收
    return data


def query_acct():  # 查询账户
    acct_no = input("请输入要查询的账户：")
    if acct_no and acct_no != "":  # 非空串
        msg = "query::" + acct_no
    else:
        msg = "query::all"  # 查询所有

    if send_msg(msg) < 0:  # 调用函数发送请求
        print("发送失败")
        return

    data = recv_msg()  # 调用函数接收查询结果
    if not data:
        print("查询失败！")
    else:
        print(data.decode())  # 打印查询结果


def new_acct():  # 新增账户
    try:
        acct_no = input("请输入帐号：")
        acct_name = input("请输入账户名：")
        acct_type = input("请输入账户类型(1－借记卡，２－理财卡)")
        balance = float(input("请输入开户金额："))
        assert balance > 10.000000
        assert (acct_type == '1' or acct_type == '2')
    except ValueError:
        print('数据格式有误')
    except AssertionError:
        print('输入值的范围有误')
    except:
        print('输入处理错误')
    else:
        msg = 'new::%s::%s::%s::%.f' % \
              (acct_no, acct_name, acct_type, balance)
        print(msg)

        if send_msg(msg) < 0:  # 发送数据
            print('发送失败')
            return

        data = recv_msg()  # 接收响应
        if not data:
            print('接收数据失败')
        else:
            print(data.decode())


def update_acct():
    global msg
    acct_no = input("请输入要修改的账户：")
    update_choose = input("请选择要修改的项：")
    update_infos = input("请输入要修改的内容:")

    if acct_no and acct_no != "":  # 非空串
        msg = "update::{}::{}::{}::%.f" \
            .format(acct_no, update_choose, update_infos)
    else:
        msg = "update::all"  # 修改所有

    if send_msg(msg) < 0:  # 调用函数发送请求
        print("发送失败")
        return

    data = recv_msg()  # 调用函数接收删除结果
    if not data:
        print("修改失败！")
    else:
        print(data.decode())  # 打印查询结果


def del_acct():
    global msg
    acct_no = input("请输入要删除的账户：")
    if acct_no and acct_no != "":  # 非空串
        msg = "delete::" + acct_no  # type: str

    if send_msg(msg) < 0:  # 调用函数发送请求
        print("发送失败")
        return

    data = recv_msg()  # 调用函数接收删除结果
    if not data:
        print("删除失败！")
    else:
        print(data.decode())  # 打印查询结果


def main():  # 客户端总入口
    open_coon()  # 连接服务器
    while True:
        print_menu()  # 打印菜单
        oper = input("请输入要执行的操作：")
        if not oper:
            continue
        elif oper == '1':  # 查询
            query_acct()
        elif oper == '2':  # 新增
            new_acct()
        elif oper == '3':
            update_acct()
        elif oper == '4':
            del_acct()
        elif oper == '5':
            break
        else:
            print('请正确输入！！！')


if __name__ == '__main__':
    main()
