# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 9:57
# @File_name:class_exercise_send.py
# @IDE:PyCharm

'''
L = [1,2,3]
def f1(list):     #  创建一个局部变量
    L = list
    print(L)
def f2(list):     #出错 ，不可对全局进行赋值
    L += list
def f3(list):     #  直接对全局变量的列表进行操作
    L.extend(list)

f1([4,5,6])

#f2([4,5,6])
f3([4,5,6])
print(L)
'''

'''
# 1.写一个lambda表达式
# fx = lambda n: .....
# 此表达式创建的函数判断n这个数的平方 + 1
# 能否被5整除,
# 如果能整除则返回True, 否则返回False
# print(fx(3))  # True
# print(fx(4))  # False

fx = lambda n: (n**2 + 1) % 5 == 0
# def fx(n):
#   return (n**2 + 1) % 5 == 0

print(fx(3))  # True
print(fx(4))  # False
'''


'''
# 2.写一个lambda
# 表达式来创建函数, 此函数返回两个参
# 数的最大值
# def mymax(x, y):
#     ....
# mymax = lambda .....
# print(mymax(100, 200))  # 200

# mymax = lambda x,y :x if x > y else y    # 条件表达式
# print(mymax(100, 200))  # 200
'''


'''
# 3.看懂下面的程序在做什么?结果是什么 ?
# def fx(f, x, y):
#     print(f(x, y))
# fx((lambda a, b: a + b), 100, 200)
# fx((lambda x, y: x ** y), 3, 4)

def fx(f, x, y):
    print(f(x, y))
fx((lambda a, b: a + b), 100, 200)
fx((lambda x, y: x ** y), 3, 4)
'''