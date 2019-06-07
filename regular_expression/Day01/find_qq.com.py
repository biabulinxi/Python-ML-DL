# @Project:AID1810
# @Author:biabu
# @Date:18-12-18 上午9:17
# @File_name:find_qq.com.py
# @IDE:PyCharm

s = "3094333@qq.com aaa@126.com 555555@qq.com"

# 用splite方法切割
rList = s.split(" ")
for r in rList:
    if r[-6:] == "qq.com":
        print(r)


# 正则表达式
import re

qq = re.findall('\d+@qq.com', s) # 返回的是一个列表
print(qq)

s = "30964@qq.comwang@126.comwei@163.commeng@tedu.cn"

email = re.findall("\w+@\w+\.com|\w+@\w+\.cn",s)
email1 = re.findall("\w+@\w+\.co?\w",s)
print(email)
print(email1)