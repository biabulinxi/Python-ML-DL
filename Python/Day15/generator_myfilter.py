# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 上午11:42
# @File_name:generator_myfilter.py
# @IDE:PyCharm

def myfilter(fn,iterable):

    for i in iterable:
        if fn(i):
            yield i

for i in myfilter(lambda y: y%2 == 1,range(10)):
    print(i)
