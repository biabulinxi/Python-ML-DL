# @Project:AID1810
# @Author:biabu
# @Date:18-11-23 下午2:12
# @File_name:class_human.py
# @IDE:PyCharm

class Human:
    def set_info(self, n, a,addr="不详"):
        '''此方法用来给对象添加‘姓名’，‘年龄’，‘家庭住址‘等属性’'''
        self.name = n
        self.age = a
        self.address = addr

    def show_info(self):
        '''此处显示人此的信息'''
        print(self.name,'今年',self.age,'岁,家庭住址：',self.address)

s1 = Human()
s1.set_info('小张', 20, '北京市东城区')
s2 = Human()
s2.set_info('小李', 18)
s1.show_info()  # 小张 今年 20 岁,家住: ...
s2.show_info()  # 小李 今年 18 岁,家住: 不详