# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 上午10:19
# @File_name:myeven.py
# @IDE:PyCharm

def myeven(start, stop):
    i = start
    while i < stop:
        if i % 2 == 0:
            yield i
        i += 1

for x in myeven(1, 10):
    print(x)  # 打印 [2,4,6,8]

L = [x**2 for x in myeven(10,20)]
print(L)   #[100,144...]

it = iter(myeven(3,10))
print(next(it)) #4
print(next(it)) #6
print(next(it)) #8
print(next(it)) #StopIteration