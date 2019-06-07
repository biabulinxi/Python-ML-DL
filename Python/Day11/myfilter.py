# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 11:15
# @File_name:myfilter.py
# @IDE:PyCharm


L = [i for i in filter(lambda x: x % 2 == 0,range(1,21))]
print(L)
