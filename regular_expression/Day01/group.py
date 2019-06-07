# @Project:AID1810
# @Author:biabu
# @Date:18-12-18 下午5:25
# @File_name:group.py
# @IDE:PyCharm

import re

s = "A B C D"
# r1:['A B', 'C D']
r1 = re.findall("\w+\s+\w+",s)
print(r1)

# r2:# ['A', 'C']
# 第一步:['A B', 'C D']
# 第二步:['A', 'C']
r2 = re.findall("(\w+)\s+\w+",s)
print(r2)

# r2:# [('A', 'B'), ('C', 'D')]
# 第一步:['A B', 'C D']
# 第二步:[('A', 'B'), ('C', 'D')]
r2 = re.findall("(\w+)\s+(\w+)",s)
print(r2)

# 嵌套分组：由外向内，由左向右
r4 = re.findall("((\w+)\s+)(\w+)",s).groups()
print(r4)
# 第一步分组：(\w+\s+)
# 第二步分组：((\w)+\s+)
# 第三步分组：((\w)+\s+)(\w+)