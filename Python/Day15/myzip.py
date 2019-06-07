# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 下午2:59
# @File_name:myzip.py
# @IDE:PyCharm

#方法一
def myzip(iter1, iter2):
    for i in range(min(len(iter1),len(iter2))):
        yield (iter1[i],iter2[i])

d = dict(myzip( "ABC", "123" ))
print(d)

for i in zip({1,2,3},[4,5,6]):
    print(i)

for i in myzip({1,2,3},[4,5,6]):
    print(i)