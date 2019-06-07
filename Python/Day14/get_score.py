# @Project:AID1810
# @Author:biabu
# @Date:18-11-20 上午11:04
# @File_name:get_score.py
# @IDE:PyCharm

def get_score():

    try:
        stu_input = int(input("请输入成绩："))
        if 0 <= stu_input <= 100:
            return stu_input
        else:
            return 0
    except:
        return 0

score = get_score()
print("学生的成绩是:", score)
