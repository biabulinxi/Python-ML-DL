# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/7 13:38
# @File_name:numpy_create_array.py
# @IDE:PyCharm

import numpy as np

# 创建一维数组矩阵
# 定义元素数据类型
"""
名称	                |            描述
--------------------|----------------------------------
bool	            |  用一个Bit存储的布尔类型（True或False）
inti	            |  由所在平台决定其大小的整数（一般为int32或int64）
int8	            |  一个字节大小，-128 至 127
int16	            |  整数，-32768 至 32767
int32	            |  整数，-2 ** 31 至 2 ** 32 -1
int64	            |  整数，-2 ** 63 至 2 ** 63 - 1
uint8	            |  无符号整数，0 至 255
uint16	            |  无符号整数，0 至 65535
uint32	            |  无符号整数，0 至 2 ** 32 - 1
uint64	            |  无符号整数，0 至 2 ** 64 - 1
float16	            |  半精度浮点数：16位，正负号1位，指数5位，精度10位
float32	            |  单精度浮点数：32位，正负号1位，指数8位，精度23位
float64或float	    |  双精度浮点数：64位，正负号1位，指数11位，精度52位
complex64	        |  复数，分别用两个32位浮点数表示实部和虚部
complex128或complex |  复数，分别用两个64位浮点数表示实部和虚部
--------------------|------------------------------------------ 
作者：-柚子皮- 
来源：CSDN 
原文：https://blog.csdn.net/pipisorry/article/details/39215089 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
a = np.array([2, 3, 4], dtype=np.int)
print(a)
print(a.dtype)   # 获得数据类型

# 创建二维数组矩阵
b = np.array([[2, 3, 4], [4, 5, 6]], dtype=np.int)
print(b)

# 创建零矩阵
array_zeros = np.zeros((3,4))   # 定义零矩阵的形状为三行四列
print(array_zeros)

# 创建矩阵元素全部为1
array_1 = np.ones((2,3),dtype=np.int16)
print(array_1)

# 创建空矩阵(接近于零的矩阵)
array_empty = np.empty((3,4))
print(array_empty)

# 生成有序一维数组
arrar_arange = np.arange(10,20,2)
# 生成有序一维数组，并重新定义形状
arrar_arange1 = np.arange(12).reshape((3,4))
print(arrar_arange)
print(arrar_arange1)

# 生成线段
array_line = np.linspace(1,20,5)
print(array_line)

