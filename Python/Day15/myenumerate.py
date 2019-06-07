# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 下午2:46
# @File_name:myenumerate.py
# @IDE:PyCharm



def myenumerate(iterable, start=0) :
    i = start
    for x in iterable:
        yield (i,x)
        i += 1

d = dict(myenumerate( "ABCDE", 1) )
print(d)

