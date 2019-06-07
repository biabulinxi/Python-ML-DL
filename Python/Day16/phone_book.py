# @Project:AID1810
# @Author:biabu
# @Date:18-11-22 下午3:36
# @File_name:phone_book.py
# @IDE:PyCharm

import os

#os.mknod('phone_book.txt')
f = open('phone_book.txt','a')
while True:
    name = input("name:")
    if name == '':
        break
    phone_num = input("num:")
    str1 = name + ',' + phone_num + '\n'
    f.writelines(str1)
f.close()