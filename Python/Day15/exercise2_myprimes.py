# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 下午6:04
# @File_name:exercise2_myprimes.py
# @IDE:PyCharm

def isprime(x):            #排除法
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def myprimes(n):
    x = 0
    count = 0
    while count <= n:
        if isprime(x):
            yield x
            count += 1
        x += 1

    # primes = []
    # for i in iter(x for x in range(100) if isprime(x)):
    #     primes.append(i)
    #     if len(primes) == n:
    #         yield primes


for j in myprimes(5):
    print(j)