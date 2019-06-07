# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 下午6:30
# @File_name:exercise3.py
# @IDE:PyCharm

list1 = []
while True:
    s = input("输入任意文字")
    if s == "":
        break
    list1.append(s)
for j in enumerate(list1,1):
    print("第%d行:%s" % j)
