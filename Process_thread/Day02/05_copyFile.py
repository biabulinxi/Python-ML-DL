# @Project:AID1810
# @Author:biabu
# @Date:18-12-20 下午4:11
# @File_name:05_copyFile.py
# @IDE:PyCharm

import os


# 需求：上半部分passwd1 下半部分passwd2
# 复制上半部分
def copy1():
    with open("passwd", 'r') as fr:
        with open("passwd1", 'w') as fw:
            size = os.path.getsize('passwd')
            n = size // 2
            while True:
                if n < 1024:
                    data = fr.read(n)
                    fw.write(data)
                    break
                else:
                    data = fr.read(1024)
                fw.write(data)
                n -= 1024


# 复制下半部分
def copy2():
    with open("passwd", 'r') as fr:
        with open("passwd1", 'w') as fw:
            size = os.path.getsize('passwd')
            n = size // 2
            # 光标
            fr.seek(n, 0)  # ０表示开始位置，表示往后移动n个字节
            while True:
                    data = fr.read(n)
                    if not data:
                        break
                    fw.write(data)



if __name__ == "__main__":
    pid = os.fork()
    if pid < 0:
        print("失败")
    elif pid == 0:
        copy2()
    else:
        copy1()
