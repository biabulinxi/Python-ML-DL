# @Project:AID1810
# @Author:biabu
# @Date:18-11-26 下午5:48
# @File_name:student.py
# @IDE:PyCharm

class Student:
    def __init__(self, name, age, score=None):
        '''定义学生初始属性'''
        self.__name = name
        self.__age = int(age)
        self.__score = int(score)

    def get_infos(self):
        return (self.__name,self.__age,self.__score)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_score(self,score):
        assert 0 <= score <= 100, '成绩超出范围'
        self.__score = score

    def set_age(self,age):
        assert 0 <= age <= 100, '年龄超出范围'
        self.__age = age

    def write_file(self,f):
        print(self.__name + " " + str(self.__age) +
              " " + str(self.__score) + "\n",file=f,end="")


