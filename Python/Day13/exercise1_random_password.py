# @Project:AID1810
# @Author:biabu
# @Date:2018-11-19 21:50
# @File_name:exercise1_random_password.py 
# @IDE:PyCharm

import random as R

'''
num = R.randint(0,9)
lowercase = chr(R.randint(97,122))
uppercase = chr(R.randint(65,90))

while True:
    i = R.randint(0,9)
    j = R.randint(0,9)
    k = R.randint(0,9)
    password = str(num)*i + str(lowercase)*j + str(uppercase)*k
    if len(password) == 6:
        print(password)
        break
'''
L = [i for i in range(0,10)]
L += [chr(i) for i in range(97,123)]
L += [chr(i) for i in range(65,91)]
str1 = ''
i = 0
while i <= 6:
    num = R.choice(L)
    str1 += str(num)
    i += 1

print(str1)