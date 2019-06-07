import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
s1 = pd.Series(data=[90,86,70],index=['leo','kate','john'])
print(s1)

# 通过绝对位置查找
print(s1[0])
# 通过标签查找
print(s1['leo'])
# 通过列表查找
print(s1[['leo','kate']])
# 通过表达式查找
print(s1[s1>80])

# 2.numpy中的ndarray：
s2 = pd.Series(data=np.random.randn(5),index=list('ABCDE'))
print(s2)

# 3.数字创建
num = pd.Series(data=6)
print(num)

# 4.创建一组DataFrame数据-date_range创建时间
date = pd.date_range('20100101',periods=6)
data = np.random.randn(6,4)  # 生成随机标准正态分布的数据
df = pd.DataFrame(data=data,columns=list('abcd'),index=date)
print(df)

# 查看属性
print(df.values)  # 元素
print(df.index)   # 行索引
print(df.columns)   # 列索引
print(df.shape)   # 形状
print(df.dtypes)  # 数据类型
print(df.size)    # 大小
print(df.ndim)    # 维度

# 查找单列数据
print(df.a)
print(df['a'])
# 查找多列的数据
print(df[['a','b']])

# 访问前三行数据
print(df[0:3])
print(df.head(3))  # 默认5行

# DataFrame 切片查找
# 查找前四行，前两列的数据
# loc : 只接受名称
print(df.loc['2010-01-01':'2010-01-04',['a','b']])
# iloc: 只接受索引
print(df.iloc[:4,:2])
# ix: 名称索引都接受,还可接收表达式
print(df.ix['2010-01-01':'2010-01-04',['a','b']])
print(df.ix[:4,:2])

# 获取2010-01-04之前的数据
print(df.ix[df.index < '2010-01-04'])