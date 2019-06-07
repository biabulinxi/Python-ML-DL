# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 19:53
# @File_name:exercise3_stu_mag.py
# @IDE:PyCharm

def input_student():
    L = []
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生成绩："))
        d = {}
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L


def output_student(L):
    print("| 5) 按学生成绩高-低显示学生信息   |")
    print("| 6) 按学生成绩低-高显示学生信息   |")
    print("| 7) 按学生年龄高-低显示学生信息   |")
    print("| 8) 按学生年龄低-高显示学生信息   |")
    user_input = input('请选择：')

    if user_input == '5':
        L = sorted(L, key=lambda d: d['score'], reverse=True)
    elif user_input == '6':
        L = sorted(L, key=lambda d: d['score'])
    elif user_input == '7':
        L = sorted(L, key=lambda d: d['age'],reverse=True)
    elif user_input == '8':
        L = sorted(L, key=lambda d: d['age'])

    print('+---------+-------+-------+')
    print('|  name   |  age  | score |')
    print('+---------+-------+-------+')

    for d in L:
        info = (d['name'].center(9),str(d['age']).center(7),str(d['score']).center(7))
        line = "|%s|%s|%s|" % info
        print(line)

    print('+---------+-------+-------+')


def show_menu():
    print("+--------------------------------+")
    print("| 1) 添加学生信息                 |")
    print("| 2) 查看学生信息                 |")
    print("| 3) 删除学生信息                 |")
    print("| 4) 修改学生成绩                 |")
    print("| q) 退出学生系统                 |")
    print("+---------------------------------+")


def delete_infos(infos):
    del_stu_name = input('请输入删除的学生姓名：')
    for i in infos:
        if i['name'] == del_stu_name:
            infos.remove(i)
            return
        print(del_stu_name,'不存在')


def modify_student_infos(infos):
    modify_stu_name = input('请输入修改信息的学生姓名：')
    for i in infos:
        if i['name'] == modify_stu_name:
            print('1）修改年龄：')
            print('2）修改成绩：')
            user_choice = input('请选择：')
            if user_choice == '1)':
                age = input("请输入修改后年龄：")
                i['age'] = age
            elif user_choice == '2)':
                score = input("请输入修改后的成绩：")
                i['score'] = score
            return
    print(modify_stu_name,'不存在')

# def output_by_score_ascend(L):
#     def get_score(d):
#         return d['score']
#     L2 = sorted(L,key=get_score)
#     output_student(L2)

def main():
    infos = []
    while True:
        show_menu()
        user_input = input('请选择：')
        if user_input == '1':
            infos += input_student()
        elif user_input == '2':
            output_student(infos)
        elif user_input == '3':
            delete_infos(infos)
        elif user_input == '4':
            modify_student_infos(infos)
        elif user_input == 'q':
            break

main()
