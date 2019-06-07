# @Project:AID1810
# @Author:biabu
# @Date:18-12-13 下午8:01
# @File_name:bubble_sort.py
# @IDE:PyCharm


def bubble(lst):
    # 外层循环：循环次数
    for i in range(len(lst) - 1):
        # 设置标志位
        flag = False
        # 内层循环：交换次数
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                # 若前者大于后者，则交换
                lst[j], lst[j+1] = lst[j+1],lst[j]
                flag = True
        if flag == False:
            break

    print("排序后",lst)


# recursion

def bubble_recu(lst):
    # 递归退出条件
    flag = False
    # 内层循环：交换次数
    for j in range(len(lst) - 1):
        if lst[j] > lst[j + 1]:
            # 若前者大于后者，则交换
            lst[j], lst[j+1] = lst[j+1],lst[j]
            flag = True
    if flag == False:
        print("排序后", lst)
        return
    return bubble_recu(lst)


# 原始数据
list1 = [150, 120, 170, 160, 172, 144, 187, 200, 178, 166]
print('原数据',list1)
# 排序
# bubble(list1)
# 递归冒泡
bubble_recu(list1)