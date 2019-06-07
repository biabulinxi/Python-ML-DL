# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 上午11:19
# @File_name:generator_exercise.py
# @IDE:PyCharm

'''
#生成器函数
def square_add_1(lst):
    for i in lst:
        yield i**2 + 1

L = [2, 3, 5, 7]
for i in square_add_1(L):
    print(i)

#生成器表达式
for i in (i**2 + 1 for i in L):
    print(i)

#list
list1_square_add_1 = list(map(lambda i: i**2 +1,L))
# for i in L:
#     list1_square_add_1.append(i**2 + 1)
print(list1_square_add_1)
'''

'''
numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
for t in zip(numbers, names):
    print(t)
         # 结果
         # (10086, '中国移动')
         # (10000, '中国电信')
         # (10010, '中国联通')
for t in zip(numbers, names, range(1, 10000)):
    print(t)
'''

