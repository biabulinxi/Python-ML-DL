# @Project:AID1810
# @Author:biabu
# @Date:18-12-18 上午10:09
# @File_name:re_eg.py
# @IDE:PyCharm

import re

s = "Hello 13811111111 I am 13911111111, " \
    "he is 119, hello 119."

rList = re.findall('\d{11}',s)
print(rList)
