# @Project:AID1810
# @Author:biabu
# @Date:2018/11/16 10:08
# @File_name:mydeco1.py
# @IDE:PyCharm

def mydeco(fn):
    def fx():
        print('+++++++++++++++++')
        fn()
        print('-----------------')
    return fx
@ mydeco     # 等效于第18行代码
def myfun():
    ''' 此 函 数 是 被 饰 函 数 '''
    print("myfun被调用")

# myfun = mydeco(myfun)

myfun()
myfun()
myfun()