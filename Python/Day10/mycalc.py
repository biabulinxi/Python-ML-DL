# @Project:AID1810
# @Author:biabu
# @Date:2018/11/14 10:12
# @File_name:mycalc.py
# @IDE:PyCharm


def myadd(x,y):
    return x + y

def mysub(x,y):
    return x - y

def mymul(x,y):
    return x * y

def mydiv(x,y):
    return x / y

def get_func(s):
    if s == ('+' or '加'):
        return myadd
    elif s == ('-' or '减'):
        return mysub
    elif s == ('*' or '乘'):
        return mymul
    elif s == ('/' or '除'):
        return mydiv
def main():
    while True:
        s = input("请输入计算公式: ") # 1 加 2
        # L = s.split()  # L = ['1', '加', '2']
        # a = int(L[0])
        # b = int(L[2])
        #fn = get_func(L[1])
        a = int(s[0])
        b = int(s[2])
        fn = get_func(s[1])
        print("结果是:", fn(a, b))  # 结果是:3

main()  # 调用主函数
