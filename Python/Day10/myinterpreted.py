# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 16:37
# @File_name:myinterpreted.py
# @IDE:PyCharm


Local_dict = {}
while True:
    user_input = input("请输入程序：>>>")
    if user_input == 'quit()':
        break
    exec(user_input,None,Local_dict)

print(Local_dict)         # 输入的程序变量存放于当前作用域