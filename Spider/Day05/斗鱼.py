# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/4 18:39
# @File_name:斗鱼.py
# @IDE:PyCharm

from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()
url = 'https://www.douyu.com/directory/all'
driver.get(url)

pages = input(' 请输入爬取的页数')

for i in range(int(pages)):
    rList = driver.find_elements_by_xpath('//div[@class="DyListCover-content"]')
    for r in rList:
        with open('斗鱼.csv','a',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(r.text.split('\n'))

    if driver.page_source.find('dy-Pagination-disabled') == -1:
        driver.find_element_by_class_name('dy-Pagination-next').click()
        time.sleep(2)
    else:
        break

driver.quit()
