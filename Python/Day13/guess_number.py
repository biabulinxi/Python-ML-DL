# @Project:AID1810
# @Author:biabu
# @Date:18-11-19 上午11:59
# @File_name:guess_number.py
# @IDE:PyCharm

import random as R


x = R.randint(0, 100)
count = 0
while True:
    y = int(input("请输入1-100之间的一个数字："))
    if y > x:
        print("您猜大了！")
    elif y < x:
        print("您猜小了！")
    elif y == x:
        print("恭喜您猜对了！")
        print("您猜了%d次"% (count + 1))
        break
    count += 1


