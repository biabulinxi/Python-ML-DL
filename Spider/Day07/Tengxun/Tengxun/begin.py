# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/6 11:18
# @File_name:begin.py.py
# @IDE:PyCharm

from scrapy import cmdline

# cmdline.execute('scrapy crawl daomu -o daomu.json'.split())
# cmdline.execute('scrapy crawl daomu -o daomu.csv'.split())
cmdline.execute('scrapy crawl tengxun'.split())
