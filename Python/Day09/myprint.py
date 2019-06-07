# @Project:AID1810
# @Author:biabu
# @Date:2018/11/13 15:33
# @File_name:myprint.py
# @IDE:PyCharm

def myprint(*args,sep=' ',end='\n',**kwargs):
    #设置标志位，当第二次输出时，加sep分隔符
    flag = False  # 若不为第一次输出，则为True
    for i in args:
        s = str(i)    #将args中的元素转成字符串输出
        if flag:
            print(sep,end='')  #第一次输出sep分隔符，不换行
        print(s,end='')        #第一次输出单个元素
        flag = True            #进行标志，此后循环输出不为第一次
    # 整体输出完成，进行换行，end=''是将原print函数中的end置空
    print(end,end='')

myprint(1,2,3,4)
myprint(1,2,3,4,sep='#')
myprint(1,2,3,4,end=' ')


print(1,2,3,4)
print(1,2,3,4,sep='#')
print(1,2,3,4,end=' ')