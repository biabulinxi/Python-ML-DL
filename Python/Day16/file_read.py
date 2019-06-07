# @Project:AID1810
# @Author:biabu
# @Date:18-11-22 上午10:23
# @File_name:file_read.py
# @IDE:PyCharm

try:
    #文件打开
    f = open("myfile.txt")
    print("文件打开成功")

    # 文件读取
    s = f.read()
    print(s)
    print("len(s)=",len(s))

    # 文件关闭
    f.close()
except OSError:
    print("文件打开失败")