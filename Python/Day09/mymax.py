# @Project:AID1810
# @Author:biabu
# @Date:2018/11/13 11:41
# @File_name:mymax.py
# @IDE:PyCharm

# #方法一
# def mymax(*args):
#     return max(args)

# #方法二
# def mymax(*args):
#
#     if len(args) == 1:
#         iterable = args[0]
#         max1 = iterable[0]
#         for i in iterable:
#             if i > max1:
#                 max1 = i
#         return max1
#     else:
#         max1 = args[0]
#         for i in args:
#             if i > max1:
#                 max1 = i
#
#         return max1

#方法三
def mymax(iterable,*args):

    if len(args) == 0:            #只传递一个：列表等序列
        max1 = iterable[0]        #令其第一个元素最大
        for i in iterable:        #遍历比较大小
            if i > max1:
                max1 = i
        return max1

    max1 = iterable               #传递两个以上元素
    for i in args:
        if i > max1:
                max1 = i
    return max1


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))  # 200
print(mymax(1, 3, 5, 9, 7))  # 9
#print(mymax())   # 报错

print(max([6, 8, 3, 5]))  # 8
print(max(100, 200))  # 200
print(max(1, 3, 5, 9, 7))  # 9
#print(max())   # 报错