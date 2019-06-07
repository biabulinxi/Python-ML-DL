# # @Project:AID1810
# # @Author:biabu
# # @Date:18-12-19 上午11:01
# # @File_name:re_modul.py
# # @IDE:PyCharm
#
import re

#
# # re.findall()
# from typing import List, Any
#
# pattern = r'\w+:\d+'
# s = '金毛狮王:1950 紫衫龙王:1949'
# rList = re.findall(pattern, s)
# print(rList)
#
#
# # regex.findx()
# regex = re.compile(pattern)
# rList1 = regex.findall(s, pos=2, endpos=8)  # type: List[Any]
# print(rList1)
#
# # split()
# regex = re.compile('\s+')
# rSplit = regex.split('hello world hello tarena')
# print(rSplit)
#
# s = 'hello world hello tarena'
# sList = s.split(' ')
# print(sList)
#
# # sub()
# regex = re.compile(r'\s+')
# rSub = regex.sub('###','hello world hello',1)
# print(rSub)   # hello###world hello
#
# # subn
# rSub = regex.subn('###','hello world hello',1)
# print(rSub)   # ('hello###world hello', 1)
#
# # finditer()
# rIter = re.finditer(r'\d+','2019 来了,2018 啥也没干')
# print(rIter)
# # finditer()返回结果为迭代器，遍历出来的是match对象
# # 利用match对象的group()方法获取内容　
# for r in rIter:
#     print(r)
#     print(r.group())
#
# # match()
# rMatch = re.match(r'[A-Z]\w+','Hello world')
# print(rMatch.group())
#
# # fullmatch()
# rMatch = re.fullmatch(r'[A-Z]\w+','Helloworld')
# print(rMatch.group())
#


# # search()
# rSearch = re.search(r'\d+','Hello 123 I am 456')
# try:
#     print(rSearch.group())
# except AttributeError as e:
#     print("没匹配到内容")

# match对象的方法
rGroup = re.search(r'(?P<monkey>\w+)\s(?P<elephant>\w+)',
                   'A B C D')
print(rGroup.group(0))  # A B
print(rGroup.group(1))  # A
print(rGroup.group(2))  # B
print(rGroup.groupdict())  #{'monkey':'A','elephant':'B'}
print(rGroup.groups())  # ('A', 'B')
