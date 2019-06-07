# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/4 16:21
# @File_name:05_京东商品抓取.py
# @IDE:PyCharm

from selenium import webdriver
import time
import csv

# 创建浏览器对象
# opt = webdriver.ChromeOptions()
# opt.set_headless()
driver = webdriver.Chrome()

# 访问京东
url = 'https://www.jd.com/'
driver.get(url)
# 接收终端输入
key = input("请输入要搜索的商品：")
driver.find_element_by_class_name('text').send_keys(key)
# 点击搜索
driver.find_element_by_class_name('button').click()

for i in range(5):
    # 执行js脚本，把进度条拉倒最底部
    driver.execute_script(
        'window.scrollTo(0,document.body.scrollHeight)'
    )

    # 获取商品信息
    goods = driver.find_elements_by_xpath('//div[@id="J_goodsList"]/ul/li')
    for goods in goods:
        # text 获取所有子孙节点的文本内容
        info = goods.text.split('\n')
        if info[1] == "拍拍":
            name = info[2].strip()
            price = info[0].strip()
            commit = info[3].strip()
            shop = info[4].strip()
        else:
            name = info[1].strip()
            price = info[0].strip()
            commit = info[2].strip()
            shop = info[3].strip()

        d = {
            'price':price,
            'name':name,
            'commit':commit,
            'shop':shop,
        }

        with open('京东.json','a',encoding='utf-8') as f:
            f.write(str(d)+'\n')


    # 是否点击下一页
    if driver.page_source.find('pn-next disabled') == -1:
        driver.find_element_by_class_name('pn-next').click()
        time.sleep(2)
    else:
        break

driver.quit()

