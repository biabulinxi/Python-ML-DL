# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/8 10:05
# @File_name:02_list.py
# @IDE:PyCharm

from timeit import Timer


def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li = li + [i]


def test3():
    li = [i for i in range(10000)]


def test4():
    li = list(range(10000))


def test5():
    li = []
    for i in range(10000):
        li.extend([i])


# Timer()类 测试时间
timer1 = Timer('test1()','from __main__ import test1')
print('append:',timer1.timeit(1000))

timer2 = Timer('test2()','from __main__ import test2')
print('+:',timer2.timeit(1000))

timer3 = Timer('test3()','from __main__ import test3')
print('generator:',timer3.timeit(1000))

timer4 = Timer('test4()','from __main__ import test4')
print('type:',timer4.timeit(1000))

timer5 = Timer('test5()','from __main__ import test5')
print('extend:',timer5.timeit(1000))


def test6():
    li = []
    for i in range(10000):
        li.append(i)


def test7():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer6 = Timer('test6()','from __main__ import test6')
print('append:',timer6.timeit(1000))

timer7 = Timer('test7()','from __main__ import test7')
print('insert:',timer7.timeit(1000))
