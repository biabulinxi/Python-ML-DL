# @Project:AID1810
# @Author:biabu
# @Date:18-12-7 下午2:40
# @File_name:setsockopt.py
# @IDE:PyCharm


from socket import *
address = ("0.0.0.0",9999)

#创建
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# SO_REUSEADDR 设置端口复用

# 绑定
s.bind(address)
print("family",s.family)  #地址类型
print("type",s.type)     #套接字类型
print("getsockname",s.getsockname())  #取地址
print("fileno！！！：",s.fileno())    #文件描述符
#获取SO_REUSEADDR选项值
print("getsockopt",
      s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

s.close()