# @Project:AID1810
# @Author:biabu
# @Date:18-11-22 下午5:56
# @File_name:exercise1_mycope.py
# @IDE:PyCharm


'''
import os

def mycopy(file=''):
    try:
        f1 = open(file)
        f1_name = ''
        for i in file:
            if i == '.':
                break
            f1_name += i
        f1_content = f1.read()
    except:
        print('f1打开失败')
    finally:
        f1.close()
    try:
        os.mknod('%s_copy.txt' % f1_name)
        f2 = open('%s_copy.txt' % f1_name,'a')
        for i in f1_content:
            f2_content = f2.writelines(i)
    except:
        print('复制f1失败')
    finally:
        f2.close()


mycopy('info.txt')
'''

import sys
print(sys.argv)  # sys.srgs 获取终端命令行的输入参数,返回列表

if len(sys.argv) < 3:
    print('''用法：．/mycopy 源文件路径名 目标文件路径名''')
    sys.exit()

src_file = sys.argv[1]
dst_file = sys.argv[2]

def copy_file(src,dst):

    print("正在从",src,"复制到",dst)
    try:
        # fr = open(src,'rb')
        with open(src,'rb') as fr,open(dst,'wb') as fw:
            # try:
            while True:
                b = fr.read(4096)   #次搬运4096个字节
                if not b:           # 当字节串为零,则复制完毕
                    break
                fw.write(b)
            # finally:
            #     fw.close()
        # finally:
        #     fr.close()
        print("复制成功")
    except OSError:
        print("复制失败")



copy_file(src_file,dst_file)

