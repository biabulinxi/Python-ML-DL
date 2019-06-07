# @Project:AID1810
# @Author:biabu
# @Date:18-11-20 下午3:22
# @File_name:get_age.py
# @IDE:PyCharm

def get_age():
    try:
        user_input = int(input("请输入年龄(1~140)："))
    except ValueError:
        raise ValueError('输入的不是数字')
    if user_input not in range(1,141):
        raise ValueError('用户输入的不是1~140之间的整数,获取年龄失败')
    return user_input
try:
    age = get_age()
    print("用户输入的年龄是:", age)
except ValueError as err:
    print('用户输入的不是1~140之间的整数,获取年龄失败:',err)
