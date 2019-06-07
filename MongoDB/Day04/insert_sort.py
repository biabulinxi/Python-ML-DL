# @Project:AID1810
# @Author:biabu
# @Date:18-12-17 下午7:19
# @File_name:insert_sort.py
# @IDE:PyCharm


def insert(values):
    # 外层循环，遍历所有无需数据
    for i in range(1, len(values)):
        # 取出当前无序数据
        temp = values[i]
        #　取出存放数据的插入位置
        pos = i
        # 内层循环，遍历所有有序数据
        for j in range(i-1, -1, -1):
            # 有序数据大于取出值
            if values[j] > temp:
                # 有序数据后移
                values[j+1] = values[j]
                # 更新插入位置
                pos = j
            else:
                # 则在该位置后插入数据
                pos = j + 1
                break
        #　在指定位置插入数据
        values[pos] = temp


# 原始数据
values = [80, 90, 83, 100, 96, 88, 89, 98, 85, 93]
# 调用插入排序
insert(values)
#　打印排序结果
print(values)