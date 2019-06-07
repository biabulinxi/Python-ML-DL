# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午7:48
# @File_name:quick_sort.py
# @IDE:PyCharm

def quick(values):
    # 递归退出
    if len(values) < 2:
        return values
    # 设置关键数据
    key = values[0]
    # 取出所有比key小的数据
    smaller = [x for x in values if x < key]
    # 取出所有等于key的数据
    equal = [x for x in values if x == key]
    # 取出所有比key大的数据
    bigger = [x for x in values if x > key]
    # 从小到大排列
    return quick(smaller) + equal + quick(bigger)


# 原始数据
values = [80, 90, 83, 100, 96, 88, 89, 98, 85, 93]
# 调用快速排序
values = quick(values)
#　打印排序结果
print(values)
