# @Project:AID1810
# @Author:biabu
# @Date:18-11-27 下午6:35
# @File_name:exercise2_myrange.py
# @IDE:PyCharm

class MyRangeIterator:
    def __init__(self,start,stop=None,step=1):
        self.__start = start
        self.__stop = stop
        self.__step = step

        if self.__stop is None:
            self.__stop = self.__start
            self.__start = 0

    def __next__(self):
        if self.__step > 0:
            if self.__start >= self.__stop:
                raise StopIteration
            r = self.__start
            self.__start += self.__step
            return r
        if self.__step < 0:
            if self.__start <= self.__stop:
                raise StopIteration
            r = self.__start
            self.__start += self.__step
            return r

class MyRange:
    def __init__(self,start,stop=None,step=1):
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __iter__(self):
        return MyRangeIterator(self.__start,self.__stop,self.__step)


    # def __iter__(self):
    #     if self.__stop is None:
    #         self.__stop = self.__start
    #         self.__start = 0
    #     if self.__start < self.__stop:
    #         while self.__start < self.__stop:
    #             yield self.__start
    #             self.__start += self.__step
    #     else:
    #         while self.__start > self.__stop:
    #             yield self.__start
    #             self.__start += self.__step


L = list(MyRange(5))
print(L)  # [0, 1, 2, 3, 4]
print(sum(MyRange(1, 101)))  # 5050
L2 = [x ** 2 for x in MyRange(1, 10, 3)]
print(L2)  # [1, 16, 49]
for x in MyRange(10, 0, -3):
    print(x)  # 10, 7, 4, 1
