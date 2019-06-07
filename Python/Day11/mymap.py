# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 10:05
# @File_name:mymap.py
# @IDE:PyCharm

'''
def mypower2(x, y):
    return x ** y
for x in map(mypower2, [1, 2, 3, 4], [4, 3, 2, 1]):
    print(x)
'''

'''
# x =  1**4 % 5
for x in map(pow, [1, 2, 3, 4], [4, 3, 2, 1],range(5, 10)):
    print(x)
'''

#  1. 求:1**2 + 2**2 +3**2 +...+9**2的和

'''方法一
def mypow2(x):
    return x**2
'''
'''方法二
sum1 = 0
for i in map(lambda x: x**2,range(1,10)):
    sum1 += i
print(sum1)
'''
#方法三
print(sum(map(lambda x: x**2,range(1,10))))

#  2. 求:1**3 + 2**3 +3**3 +...+9**3的和
def mypow3(x):
    return x**3
sum2 = 0
for i in map(mypow3,range(1,10)):
    sum2 += i
print(sum2)

#  3. 求:1**9 + 2**8 + 3**7 + ... + 9**1的和
sum = 0
for i in map(pow,range(1,10),range(9,0,-1)):
    sum += i
print(sum)


