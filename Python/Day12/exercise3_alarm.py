# @Project:AID1810
# @Author:biabu
# @Date:2018-11-17 17:07
# @File_name:exercise3_alarm.py 
# @IDE:PyCharm

from time import *
def alarm(user_set_time):
    while True:
        this_time = localtime()[3:6]

        alarm_time = (int(user_set_time[:2]),int(user_set_time[3:5]),int(user_set_time[6:8]))
        this_time = localtime()[3:6]

        if alarm_time == this_time:
            print("时间到！！！")
            break
        sleep(1)

user_set_time = input("请设定闹钟时间(xx:xx:xx)：")
alarm(user_set_time)

