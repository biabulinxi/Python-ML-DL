# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 下午5:47
# @File_name:exercise1_myxrange.py
# @IDE:PyCharm

def myxrange(start,stop=None,step=1):
    if stop is None:
        stop = start
        start = 0
    if start < stop:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step

sum1 = 0
for i in (i**2 for i in myxrange(1,10) if i % 2 ==1):
    sum1 += i
print(sum1)