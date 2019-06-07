# @Project:AID1810
# @Author:biabu
# @Date:18-11-23 下午6:07
# @File_name:exercise1_.py
# @IDE:PyCharm

'''
def isprime(x):            #排除法
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def fact_prime(num):
    fac_lst = []
    i = 1
    while i < num:
        if num % i == 0 and isprime(i):
            num = num // i
            if isprime(num):
                fac_lst.append(num)
            fac_lst.append(i)
        if num == 1:
            break
        i += 1
    return fac_lst
'''



def get_facts_num(n):
    '''get all facts numner'''
    L = []
    while n != 1:
        for i in range(2,n + 1):
            if n % i == 0:
                L.append(i)
                n = int(n // i)
                break
    return L

def main():
    num = int(input('请输入一个整数：'))
    str1 = '*'.join(str(i) for i in get_facts_num(num))
    print(num,'=',str1)

main()
#print(get_facts_num(56))