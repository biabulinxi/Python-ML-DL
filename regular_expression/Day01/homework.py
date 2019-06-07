# @Project:AID1810
# @Author:biabu
# @Date:18-12-19 下午3:06
# @File_name:homework.py
# @IDE:PyCharm

# 7、作业(分组)

s = """
<div class="动物">
  <p class="名字">
    <a title="兔子"></a>
  </p>
  <p class="描述">
    小白兔,白又白,两只耳朵竖起来
  </p>
</div>
<div class="动物">
  <p class="名字">
    <a title="老虎"></a>
  </p>
  <p class="描述">
    两只老虎两只老虎跑的快跑的快
  </p>
</div>
"""


# 1、提出动物和描述
#   [("兔子","  小白兔白又白..."),
#    ("老虎","  两只老虎....")]
# 2、要求输出如下结果
#   动物名称 ：兔子
#   动物描述 ：小白兔白又白...
#   **************
#   动物名称 ：老虎
#   动物描述 ：两只老虎两只老虎...

import re

pattern = '<div class="动物">.*?title="(.*?)".*?class="描述">(.*?)<.*?</div>'
regex = re.compile(pattern, re.S)
rList = regex.findall(s)
print(rList)

for r in rList:
    print('动物名称:%s' % r[0].strip())
    print('动物名称:%s' % r[1].strip())
    print('*' * 20)






