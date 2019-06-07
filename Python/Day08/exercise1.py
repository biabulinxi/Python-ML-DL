# @Project:AID1810
# @Author:biabu
# @Date:2018/11/12 17:52
# @File_name:mysum.py
# @IDE:PyCharm

def sum3(a,b,c):
    sum = a + b + c
    return sum

def pow3(x):
    return x**3

print(sum3(pow3(1),pow3(2),pow3(3)))
print(pow3(sum3(1,2,3)))