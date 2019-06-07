# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/4 14:23
# @File_name:02_selenium_phantomjs.py
# @IDE:PyCharm

from selenium import webdriver
import time

# 1.创建浏览器对象
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
# 2.利用浏览器对象的get方法发请求
driver.get('http://www.baidu.com')
# 3.获取屏幕截图
driver.save_screenshot("百度chrome.png")
time.sleep(10)
# 4.关闭浏览器
driver.quit()
