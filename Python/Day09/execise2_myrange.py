# @Project:AID1810
# @Author:biabu
# @Date:2018/11/13 18:00
# @File_name:execise2_myrange.py
# @IDE:PyCharm

def myrange(start,stop=None,step=1):
    if stop is None:
        stop = start
        start = 0
    if start < stop:
        list1 = []
        while start < stop:
            list1.append(start)
            start += step
        return list1
    else:
        list1 = []
        while start > stop:
            list1.append(start)
            start += step
        return list1
L = myrange(4)
print(L)  # [0, 1, 2, 3]
L = myrange(4,6)
print(L)  # [4, 5]
L = myrange(10, 0, -3)
print(L)  # [10, 7, 4, 1]

