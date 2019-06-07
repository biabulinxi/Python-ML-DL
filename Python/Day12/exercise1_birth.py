# @Project:AID1810
# @Author:biabu
# @Date:2018/11/16 18:12
# @File_name:exercise1_birth.py
# @IDE:PyCharm

from time import *

user_birthday = input('请输入您的生日(XXXX年XX月XX日)：')


user_bth_time = mktime((int(user_birthday[:4]), int(user_birthday[5:7]), int(user_birthday[8:10]),0,0,0,0,0,0))
this_time = mktime((localtime()[0], localtime()[1], localtime()[2],0,0,0,0,0,0))

birth_sum_days = (user_bth_time - this_time) / (60 * 60 * 24)
birthday = localtime(user_bth_time)

print("您已出生%s天" % birth_sum_days)
for i in range(8):
    if birthday[6] == i:
        d = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日'}
        print('您出生那天是星期%s' % (d[i]))

