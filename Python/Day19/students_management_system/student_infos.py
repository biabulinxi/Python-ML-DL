# @Project:AID1810
# @Author:biabu
# @Date:18-11-20 上午9:13
# @File_name:student_infos.py
# @IDE:PyCharm

from student import Student

def input_student():
    L = []
    while True:
        try:
            name = str(input("请输入学生姓名："))
            if not name:
                break
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生成绩："))
        except ValueError:
            print("格式错误,请重新输入")
        else:
            d = Student(name, age, score)
            L.append(d)
    return L


def output_student(L):

    def output_infos(lst):
        print('+----------+-------+-------+')
        print('|   name   |  age  | score |')
        print('+----------+-------+-------+')

        for d in lst:
            n,a,s = d.get_infos()
            info = (n.center(9),str(a).center(7),str(s).center(7))
            line = "|%s|%s|%s|" % info
            print(line)

        print('+---------+-------+-------+')

    print("+-----------------------------+")
    print("| 5 按学生成绩高-低显示学生信息   |")
    print("| 6 按学生成绩低-高显示学生信息   |")
    print("| 7 按学生年龄高-低显示学生信息   |")
    print("| 8 按学生年龄低-高显示学生信息   |")
    print("+-----------------------------+")

    try:
        user_input = int(input('请选择：'))
    except ValueError:
        print("格式错误，请重新输入")
    else:
        if user_input == 5:
            L = sorted(L, key=lambda d: d.get_score(), reverse=True)
            output_infos(L)
        elif user_input == 6:
            L = sorted(L, key=lambda d: d.get_score())
            output_infos(L)
        elif user_input == 7:
            L = sorted(L, key=lambda d: d.get_age(),reverse=True)
            output_infos(L)
        elif user_input == 8:
            L = sorted(L, key=lambda d: d.get_age())
            output_infos(L)
        elif user_input < 5 or user_input > 8:
                print("输入错误，请重新选择")





def delete_infos(infos):
    try:
        del_stu_name = str(input('请输入删除的学生姓名：'))
    except ValueError:
        print("格式错误，请重新输入")
    else:
        for i in infos:
            if i.get_name() == del_stu_name:
                infos.remove(i)
                print('%s删除成功' % del_stu_name)
                break
            print(del_stu_name,'不存在')


def modify_student_infos(infos):
    try:
        modify_stu_name = str(input('请输入修改信息的学生姓名：'))
    except ValueError:
        print("格式错误，请重新输入")
    else:
        for i in infos:
            if i.get_name() == modify_stu_name:
                print('1 修改年龄：')
                print('2 修改成绩：')
                user_choice = input('请选择：')
                if user_choice == '1':
                    age = int(input("请输入修改后年龄："))
                    i.set_age(age)
                elif user_choice == '2':
                    score = int(input("请输入修改后的成绩："))
                    i.set_score(score)
                else:
                    print("输入错误，请重新选择")
                return
        print(modify_stu_name,'不存在')


def read_file(file=''):
    infos =[]
    try:
        f = open(file)
        for line in f:
            line = line.strip()
            name, age, score = line.split()
            infos.append(Student(name,age,score))
        print("读取信息成功！")
        return infos
    except:
        print("读取信息失败！！！")
    finally:
        f.close()


def write_file(infos,file='stu_infos.txt'):
    try:
        f = open(file,'a')
        for i in infos:
            # method1
            # str1 = i.get_name() + " " + str(i.get_age()) + " " + str(i.get_score()) + "\n"
            # f.writelines(str1)
            #method2
            i.write_file(f)

        print("写入信息成功")
    except:
        print("写入信息失败！！！")
    finally:
        f.close()


