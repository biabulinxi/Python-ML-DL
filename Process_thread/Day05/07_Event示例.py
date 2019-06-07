# @Project:AID1810
# @Author:biabu
# @Date:18-12-25 下午2:38
# @File_name:07_Event示例.py
# @IDE:PyCharm

from threading import Event

# 创建事件对象
e = Event()

# 将e改为已设置，并打印
e.set()
print(e.is_set())

# 清除e的设置，改为未设置，并打印
e.clear()
print(e.is_set())

# 使用wait()
e.wait()
# 超时２秒
e.wait(timeout=2)

print("****************************")