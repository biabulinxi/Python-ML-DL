# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 17:51
# @File_name:exercise3_mypow.py
# @IDE:PyCharm

def mypow(n):
    ''' 方法一
    sum1 = 0
    for i in range(1,n+1):
        sum1 += i**i
    return sum1
    '''
    #方法二
    return sum(map(lambda n: n**n,range(1,n+1)))

print(mypow(3))