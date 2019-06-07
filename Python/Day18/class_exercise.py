# @Project:AID1810
# @Author:biabu
# @Date:18-11-26 下午2:44
# @File_name:class_exercise_send.py
# @IDE:PyCharm


class My_list(list):
    def insert_head(self,n):
        #self.insert(0,n)
        self[0:0] = [n]

myl = My_list(range(3,6))
print(myl)          #[3,4,5]

myl.insert_head(2)
print(myl)          #[2,3,4,5]

myl.append(6)
print(myl)          #[2,3,4,5,6]