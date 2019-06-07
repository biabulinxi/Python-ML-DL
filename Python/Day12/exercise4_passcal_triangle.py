# @Project:AID1810
# @Author:biabu
# @Date:2018-11-17 17:35
# @File_name:exercise4_passcal_triangle.py 
# @IDE:PyCharm

#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1
#  1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1

def yanghui_line(lst):
    L = [1]
    for i in range(1,len(lst)):
        L.append(lst[i] + lst[i - 1])
    L.append(1)
    return L

def print_line(lst,wth):
    str1 = ""
    for i in lst:
        str1 += str(i) + " "
    print(str1.center(wth))

def main():
    list1 = [1]
    row = int(input("请输入行数："))
    width = row * 5
    for i in range(row):
        print_line(list1,width)
        list1 = yanghui_line(list1)

if __name__ == '__main__':
    main()
