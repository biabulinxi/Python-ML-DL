# @Project:AID1810
# @Author:biabu
# @Date:18-11-20 上午9:16
# @File_name:main.py
# @IDE:PyCharm


from menu import show_menu
from student_infos import input_student,output_student,delete_infos,modify_student_infos

def main():
    infos = []
    while True:
        show_menu()
        user_input = input('请选择：')
        if user_input == '1':
            infos += input_student()
        elif user_input == '2':
            output_student(infos)
        elif user_input == '3':
            delete_infos(infos)
        elif user_input == '4':
            modify_student_infos(infos)
        elif user_input == 'q':
            break
        else:
            print("输入错误，请重新选择")

main()
