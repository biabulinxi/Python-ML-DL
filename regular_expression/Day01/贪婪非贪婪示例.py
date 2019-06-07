# @Project:AID1810
# @Author:biabu
# @Date:18-12-18 下午4:45
# @File_name:贪婪非贪婪示例.py
# @IDE:PyCharm

import re

s = """
<div>仰天大笑出门去</div>
<div>九霄龙云惊天变</div>
"""

# 贪婪匹配
result = re.findall("<div>([\s\S]*)</div>",s)
print(result)

# 非贪婪匹配
result = re.findall("<div>([\s\S]*?)</div>",s)
print(result)
