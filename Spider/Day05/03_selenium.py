# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/4 14:42
# @File_name:03_selenium.py
# @IDE:PyCharm

from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome()
# 发送请求
driver.get('http://www.baidu.com')
# 接收终端收入，放入搜索框
key = input("请输入搜索的内容:")
driver.find_element_by_id('kw').send_keys(key)
# 点击按钮进行搜索
driver.find_element_by_id('su').click()
time.sleep(5)
# 获取截图
html = driver.page_source
print(html)
driver.save_screenshot(key+'.png')
# 退出浏览器
driver.quit()
