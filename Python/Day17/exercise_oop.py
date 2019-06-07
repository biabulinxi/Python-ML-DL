# @Project:AID1810
# @Author:biabu
# @Date:18-11-23 下午4:36
# @File_name:exercise_oop.py
# @IDE:PyCharm

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.money = 0
        self.boorow_money = 0

    def teach(self,other,tech):
        self.tech = tech
        print(self.name,'教',other.name,'学',self.tech,sep='')

    def work(self,money):
        self.money += money
        print(self.name,'上班赚了',money,'元',sep='')

    def boorow(self,other,boorow_money):
        if other.money > boorow_money:
            other.money -= boorow_money
            self.money += boorow_money
            print(self.name,'向',other.name,'借了',boorow_money,'元',sep='')
        else:
            print('借钱失败！！！')
    def show_info(self):
        print(self.age,'岁的',self.name,'有钱',int(self.money),
              '元,它学会的技能是',self.tech,sep='')


human1 = Human('张三',35)
human2 = Human('李四',15)

human1.teach(human2,'Python')
human2.teach(human1,'王者荣耀')
human1.work(1000)
human2.boorow(human1,200)
human1.show_info()
human2.show_info()


