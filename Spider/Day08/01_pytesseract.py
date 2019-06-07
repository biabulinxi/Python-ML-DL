# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/7 14:49
# @File_name:01_pytesseract.py
# @IDE:PyCharm
import pytesseract
# python 图像处理库
from PIL import Image


# 创建图片对象
img = Image.open('test1.jpg')

# 图片转字符串
result = pytesseract.image_to_string(img)
print(result)

