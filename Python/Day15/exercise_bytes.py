# @Project:AID1810
# @Author:biabu
# @Date:18-11-21 下午4:55
# @File_name:exercise_bytes.py
# @IDE:PyCharm

'''
s = input("请输入一段字符串：")
b = s.encode('utf-8')
print(b)
print(len(s),len(b))

s2 = b.decode('utf-8')
if s2 == s:
    print("True")
'''


s = input("请输入一段字符串：")
b = bytearray(s,'utf-8')
print(b)
print(len(s),len(b))

s3 = b.decode('utf-8')
if s3 == s:
    print("True")