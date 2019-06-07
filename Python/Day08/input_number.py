# @Project:AID1810
# @Author:biabu
# @Date:2018/11/12 16:19
# @File_name:input_number.py
# @IDE:PyCharm


#方法一

# def input_number():
#     user_input_number = []
#     while True:
#         user_input = int(input('Please input a number'))
#         if user_input < 0:
#             break
#         user_input_number.append(user_input)
#     return user_input_number

#方法二
def input_number():
    user_input_number = []
    while True:
        user_input = int(input('Please input a number'))
        if user_input < 0:
            return user_input_number    #可直接将break换成return语句
        user_input_number.append(user_input)


L = input_number()
print(L)
print("最大数是:",max(L))
print("最小数是:",min(L))
print("和是:",sum(L))

