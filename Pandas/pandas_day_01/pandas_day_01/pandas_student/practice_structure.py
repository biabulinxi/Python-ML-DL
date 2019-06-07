"""
pandas基础
"""

import pandas as pd
import numpy as np

# 1.Series创建
s1 = pd.Series(data=[3, 5, -7, 6], index=list('ABCD'))
print(s1)

# 2.DataFrame创建
data = [['Belglum', 'Brussels', 11190846],
        ['Indla', 'New Delhi', 1303171035],
        ['Brazil', 'Brasilia', 207847528]]
# 比利时 布鲁塞尔
# 印度 新德里
# 巴西 巴西利亚

df1 = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'], index=[1, 2, 3])
print(df1)
