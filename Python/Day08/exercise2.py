# @Project:AID1810
# @Author:biabu
# @Date:2018/11/12 18:02
# @File_name:exercise2.py
# @IDE:PyCharm

def get_chinese_char_count(s):
    count = 0
    for i in s:
        if ord(i) in range(0x4E00,0x9FA5):
            count += 1                      #识别不了中文标点符号
    return count


s = input("请输入中英文混合的字符串:")
print("您输入的中文字符的个数是:",get_chinese_char_count(s))

