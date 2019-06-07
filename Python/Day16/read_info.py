# @Project:AID1810
# @Author:biabu
# @Date:18-11-22 上午11:51
# @File_name:read_info.py
# @IDE:PyCharm

try:
    f = open('info.txt')

    for i in f:
        i = i.strip()
        lst = i.split()
        name, age, score = lst
        print(name,'今年',age,'岁,成绩是：',score,sep='')
    f.close()
except OSError:
    print('文件打开失败')