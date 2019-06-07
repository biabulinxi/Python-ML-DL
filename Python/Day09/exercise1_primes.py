# @Project:AID1810
# @Author:biabu
# @Date:2018/11/13 17:42
# @File_name:exercise1_primes.py
# @IDE:PyCharm

def isprime(x):            #排除法
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


print(isprime(2))  # True
print(isprime(4))  # False


def prime_m2n(m, n):
    '''   方法一
    list2 = []
    for i in range(m,n):
        if isprime(i):
            list2.append(i)
    return list2
    '''
    #列表推导式
    return [x for x in range(m,n) if isprime(x)]


L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]


def primes(n):
    '''方法一
    list3 = []
    for i in range(n):
        if isprime(i):
            list3.append(i)
    return sum(list3)
    '''
    return sum(prime_m2n(0,n))



L = primes(100)
print(L)
L = primes(200)
print(L)