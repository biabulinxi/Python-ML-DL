# @Project:AID1810
# @Author:biabu
# @Date:2018/11/12 15:56
# @File_name:mymax.py
# @IDE:PyCharm

def mymax(a,b,c):
#  方法一
    if a < b and b < c:
        return c
    return b
    if a > b and a < c:
        return c
    return a



#  方法二
#     my_max = max(a,b,c)
#     return my_max

print(mymax(100,200,300))
print(mymax("ABC","abc","123"))

