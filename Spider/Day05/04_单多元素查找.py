# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/4 15:41
# @File_name:04_单多元素查找.py
# @IDE:PyCharm

from selenium import webdriver
import time

# 设置Chrome无界面模式
opt=webdriver.ChromeOptions()
opt.set_headless()
driver=webdriver.Chrome(options=opt)
url = 'https://www.qiushibaike.com/text/'
driver.get(url)

# 查找单个节点
rOne = driver.find_element_by_class_name('content')
print(rOne.text)

# 查找多个节点
rMany = driver.find_elements_by_class_name('content')
for r in rMany:
    print(r.text)
