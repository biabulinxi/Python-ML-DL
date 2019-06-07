# @Project:AID1810
# @Author:biabu
# @Date:18-11-20 下午5:55
# @File_name:exercise2_ball_fall.py
# @IDE:PyCharm



count = 10
initial_height = 100
list1 = []
i = 1
while i <= count:
    final_height = initial_height / 2
    journey = initial_height + final_height
    list1.append(journey)
    initial_height = final_height
    i += 1

print("皮球在第10次落后反弹%f米高" % initial_height)
print("皮球在第10次反弹后经过%f米路程" % sum(list1))


