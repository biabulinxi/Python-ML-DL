# @Project:AID1810
# @Author:biabu
# @Date:18-11-23 下午3:11
# @File_name:stu_class.py
# @IDE:PyCharm


class Student:
    def __init__(self,name,age,score=None):
        '''定义学生初始属性'''
        self.name = name
        self.age = age
        self.score = score

    def set_score(self,score):
        '''此方法可修改学生信息'''
        self.score = score

    def show_info(self):
        print(self.name,self.age,self.score)


L = []
L.append(Student('小张', 20, 100))
L.append(Student('小李', 18, 95))
L.append(Student('小钱', 19))
L[-1].set_score(70)

for s in L:
    s.show_info()
