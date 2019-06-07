# @Project:AID1810
# @Author:biabu
# @Date:18-12-5 下午5:19
# @File_name:register_login.py
# @IDE:PyCharm

from mysqlpython import MysqlPython
from hashlib import sha1



#登录
def register():
    #用户输入用户名
    uname = input("请输入用户名：")
    #到user表中查询此信息
    sele = 'select name from user where name=%s'
    r = sqlh.refer(sele,[uname])
    if len(r) != 0:
        print('该用户名已被注册！')
    else:
    #输入密码
        pwd1 = input("请输入密码：")
        pwd2 = input("请再次输入密码：")

        if pwd1 == pwd2:
            #加密存库
            s = sha1()
            s.update(pwd1.encode("utf-8"))   #加密需转为字节流
            pwd = s.hexdigest()              #转成十六进制
            ins = 'insert into user values(%s,%s)'
            sqlh.exe(ins,[uname,pwd])
            print("注册成功")
        else:
            print("密码不一致")


#　登录功能
def login():
    uname = input("请输入用户名：")
    pwd = input("请输入密码：")

    #加密
    s = sha1()
    s.update(pwd.encode("utf-8"))  # 加密需转为字节流
    pwd = s.hexdigest()  # 转成十六进制

    #　查询
    sele = 'select password from user where name=%s'
    r = sqlh.refer(sele,[uname])
    # 判断用户名
    if len(r) == 0:
        print("用户名不存在")
    #　判断密码
    elif pwd == r[0][0]:
        print('登录成功')
    else:
        print('密码错误')

sqlh = MysqlPython()
login()
