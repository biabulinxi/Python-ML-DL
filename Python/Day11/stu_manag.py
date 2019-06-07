# @Project:AID1810
# @Author:biabu
# @Date:2018/11/19 11:03
# @File_name:stu_manag.py
# @IDE:PyCharm


#   3. 改写之前的学生信息管理项目程序
#      要求添加四个功能:
#        | 5) 按学生成绩高-低显示学生信息 |
#        | 6) 按学生成绩低-高显示学生信息 |
#        | 7) 按年龄成绩高-低显示学生信息 |
#        | 8) 按年龄成绩低-高显示学生信息 |



def input_student():
    # 此函数用于返回所有用户输入的学生信息的列表
    infos = []  # 创建一个列表容器准备存放每个学生信息的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果姓名为空,则结束输入
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        # 新创建一个字典 {}  dict()
        d = {'name':n, 'age':a, 'score':s}  # d = dict(name=n, age=a, score=s)
        infos.append(d)
    return infos

def output_student(L):
    # 此函数以表格形式打印学生信息
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for d in L:  # d绑定字典
        n = d['name']
        a = d['age']
        s = d['score']
        a = str(a)  # 将整数转为字符串
        s = str(s)
        print("|" + n.center(15) + '|'
                + a.center(11) + '|'
                + s.center(10) + '|')
    print("+---------------+-----------+----------+")

def remove_student(L):
    # 获取要删除人的姓名
    n = input("请输入要删除人的姓名: ")
    i = 0  # 开始索引
    while i < len(L):
        if L[i]['name'] == n:
            del L[i]  # 删除索引
            print("删除成功!")
            return # 删除完毕
        i += i

def modify_student_score(L):
    n = input("请输入要修改成绩的人的姓名: ")
    s = int(input("请输入新成绩: "))
    print(".....")

def output_student_by_score_desc(L):
    # 生成一个排序后的新列表
    def k(d):  # 传入的是字典,返回的是成绩
        return d['score']
    lst = sorted(L, key=k, reverse=True)
    output_student(lst)

def output_student_by_score_asc(L):
    lst = sorted(L, key=lambda d: d['score'])
    output_student(lst)

def output_student_by_age_desc(L):
    lst = sorted(L,
                 key=lambda d: d['age'],
                 reverse=True)
    output_student(lst)

def output_student_by_age_asc(L):
    lst = sorted(L, key=lambda d: d['age'])
    output_student(lst)



def show_menu():
    print("+--------------------------------+")
    print("| 1) 添加学生信息                |")
    print("| 2) 查看学生信息                |")
    print("| 3) 删除学生信息                |")
    print("| 4) 修改学生成绩                |")
    print("| 5) 按学生成绩高-低显示学生信息 |")
    print("| 6) 按学生成绩低-高显示学生信息 |")
    print("| 7) 按年龄成绩高-低显示学生信息 |")
    print("| 8) 按年龄成绩低-高显示学生信息 |")
    print("| q) 退出                        |")
    print("+--------------------------------+")

def main():
    '''主函数,此函数最先运行'''
    infos = []  # 此列表用来保存所有学生的信息的字典
    # 进入主事件循环
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            return  # 退出main函数
        elif s == '1':
            infos += input_student()
            # infos.extend(input_student())
        elif s == '2':
            output_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_student_score(infos)
        elif s == '5':
            output_student_by_score_desc(infos)
        elif s == '6':
            output_student_by_score_asc(infos)
        elif s == '7':
            output_student_by_age_desc(infos)
        elif s == '8':
            output_student_by_age_asc(infos)

main()



