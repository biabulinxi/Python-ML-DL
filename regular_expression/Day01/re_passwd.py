# @Project:AID1810
# @Author:biabu
# @Date:18-12-18 上午11:15
# @File_name:re_passwd.py
# @IDE:PyCharm

import re

with open('passwd','r') as f:
    lines = f.readlines()
    for line in lines:
        resp = re.findall('^tarena',line)
        if resp:
            print(resp)

i = 0
with open('passwd','r') as f:
    lines = f.readlines()
    for line in lines:
        resp = re.findall('/usr/sbin/nologin$',line)
        if resp:
            i += 1
    print("没有登录权限的用户有%d个" % i)