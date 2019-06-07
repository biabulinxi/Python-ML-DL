# @Project:AID1810
# @Author:biabu
# @Date:18-12-13 下午7:11
# @File_name:binarysearch.py
# @IDE:PyCharm


def binary(value,key):
    # 查找范围为对应的一侧下标值
    left = 0
    right = len(value) - 1

    # 合法查找循环查找
    while left <= right:
        # 中间元素下标值
        middle = (left + right) // 2
        # 比较中间值与指定值
        if value[middle] == key:
            # 若相等，则返回
            return middle
        elif value[middle] > key:
            # 若指定值系小于中间值，
            # 则在左侧继续查找
            right = middle - 1
        else:
            # 若指定值系大于中间值，
            # 则在右侧继续查找
            left = middle + 1
    # 查找失败返回-1
    return -1

# 原始数据
values = range(1,13)
# 要查找６
key = 6

# 调用二分查找

res = binary(values,key)
if res == -1:
    print("查找失败")
else:
    print("查找成功，对应下标为：",res)