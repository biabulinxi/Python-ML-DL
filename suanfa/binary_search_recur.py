# @Project:AID1810
# @Author:biabu
# @Date:18-12-13 下午7:30
# @File_name:binary_search_recur.py
# @IDE:PyCharm

# 递归实现
# left - 当前查找对应的左侧下标值
# right - 当前查找对应的右侧下标值

def binary(value, key, left, right):
    # 查找失败，递归退出
    if left > right:
        return -1

    # 获取中间元素下标
    middle = (left + right) // 2
    # 进行比较
    if value[middle] == key:
        # 查找成功，返回下标
        return middle
    elif value[middle] > key:
        # 若指定值系小于中间值，
        # 则在左侧继续查找
        right = middle - 1
        return binary(value, key, left, right)
    else:
        # 若指定值系大于中间值，
        # 则在右侧继续查找
        left = middle + 1
        return binary(value, key, left, right)


# 原始数据
values = range(1, 13)
# 要查找６
key = 3
left = 0
right = len(values) - 1
# 调用二分查找

res = binary(values, key, left, right)
if res == -1:
    print("查找失败")
else:
    print("查找成功,对应下标为：", res)
