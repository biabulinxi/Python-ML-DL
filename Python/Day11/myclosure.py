# @Project:AID1810
# @Author:biabu
# @Date:2018/11/15 16:32
# @File_name:myclosure.py
# @IDE:PyCharm



def get_fx(a,b,c):
    def fx(x):
        return a*x**2 + b*x + c

    return fx


f234 = get_fx(2,3,4)
print("f234(20)：",f234(20))