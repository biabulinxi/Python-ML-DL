# @Project:AID1810
# @Author:biabu
# @Date:18-11-24 上午11:28
# @File_name:exercise2_.py
# @IDE:PyCharm


class Student:
    # def __init__(self,name,age,score=None):
    #     '''定义学生初始属性'''
    #     self.name = name
    #     self.age = age
    #     self.score = score

    def set_score(self,score):
        '''此方法可修改学生信息'''
        self.score = score

    def show_info(self):

        print('+----------+-------+-------+')
        print('|   name   |  age  | score |')
        print('+----------+-------+-------+')

        for d in self.L:
            info = (d['name'].center(10), str(d['age']).center(7), str(d['score']).center(7))
            line = "|%s|%s|%s|" % info
            print(line)

        print('+---------+-------+-------+')



    def input_student(self):
        self.L = []
        while True:
            try:
                self.name = str(input("请输入学生姓名："))
                if not self.name:
                    break
                self.age = int(input("请输入学生年龄："))
                self.score = int(input("请输入学生成绩："))
            except ValueError:
                print("格式错误，请重新输入")
            else:
                d = {'name':self.name,'age':self.age,'score':self.score}
                self.L.append(d)
        return self.L


    def del_student(self):
        try:
            del_name = str(input('请输入删除的学生姓名：'))
        except ValueError:
            print("格式错误，请重新输入")
        else:
            for i in self.L:
                if i['name'] == del_name:
                    self.L.remove(i)
                    return self.L
                else:
                    print(del_name,'不存在')
    def stu_tatal(self):
        print('学生个数为：',len(self.L))

student = Student()
student.input_student()
student.del_student()
student.show_info()
student.stu_tatal()



 