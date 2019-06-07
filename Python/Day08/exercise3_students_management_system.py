# @Project:AID1810
# @Author:biabu
# @Date:2018/11/12 18:25
# @File_name:exercise3_students_management_system.py
# @IDE:PyCharm

def input_student():
    L = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = input("请输入学生年龄：")
        score = input("请输入学生成绩：")
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L

def output_student(L):

    print('+---------+-------+-------+')
    print('|  name   |  age  | score |')
    print('+---------+-------+-------+')

    for d in L:
        info = (d['name'].center(9),str(d['age']).center(7),str(d['score']).center(7))
        line = "|%s|%s|%s|" % info
        print(line)

    print('+---------+-------+-------+')


infos = input_student()
print(infos)
output_student(infos)