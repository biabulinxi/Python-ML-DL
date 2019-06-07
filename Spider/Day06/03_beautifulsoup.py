# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/5 14:21
# @File_name:03_beautifulsoup.py
# @IDE:PyCharm

from bs4 import BeautifulSoup

html = '''
<div class='test>风云雄霸天下</div>'''

soup = BeautifulSoup(html,'lxml')

rList = soup.find_all('div',attrs={'class':'test'})
for r in rList:
    print(r.get_text())

