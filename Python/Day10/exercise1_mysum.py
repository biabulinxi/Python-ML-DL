# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 17:36
# @File_name:exercise1_mysum.py
# @IDE:PyCharm



def mysum(n):
    '''方法一
    sum1 = 0
    for i in range(1,n + 1):
         sum1 += i
    return sum1
    '''
    #方法二
    return sum(range(1,n+1))
print(mysum(100))  # 5050