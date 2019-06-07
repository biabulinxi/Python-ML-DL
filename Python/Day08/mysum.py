# @Project:AID1810
# @Author:biabu
# @Date:2018/11/12 16:12
# @File_name:mysum.py
# @IDE:PyCharm

def mysum(a,b):
    sum = a + b
    return sum      # return a + b

a = int(input("请输入第一个数: "))
b = int(input("请输入第二个数: "))
print("您输入的两个数的和是:",mysum(a,b))

