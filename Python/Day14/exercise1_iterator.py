# @Project:AID1810
# @Author:biabu
# @Date:18-11-20 下午4:55
# @File_name:exercise1_iterator.py.py
# @IDE:PyCharm

'''
s = {'唐僧', '悟空', '八戒', '沙僧'}
# 用for语句来遍历所有元素如下:
for x in s:
    print(x)
else:
    print("遍历结束")
# 请将上面的for语句改写为while语句和迭代器实现
'''

s = {'唐僧', '悟空', '八戒', '沙僧'}
it = iter(s)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break


