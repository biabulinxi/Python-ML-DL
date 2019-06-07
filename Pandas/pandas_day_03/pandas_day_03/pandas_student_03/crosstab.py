import pandas as pd
import numpy as np
data = pd.DataFrame({'Sample': range(1, 11), 'Gender': ['Female', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female'],
                    'Handedness': ['Right-handed', 'Left-handed', 'Right-handed', 'Right-handed', 'Left-handed', 'Right-handed', 'Right-handed', 'Left-handed', 'Right-handed', 'Right-handed']})
print(data)

# 方法一：用pivot_table
data_Handedness = pd.pivot_table(data,index='Gender',columns='Handedness',values='Sample',aggfunc=len,margins=True)
print(data_Handedness)

# 方法二：用crosstab
# crosstab()的前两个参数可以是数组、Series或数组列表
data_Handedness = pd.crosstab(index=data['Gender'],columns=data['Handedness'],values=data['Sample'],aggfunc=len,margins=True)
print(data_Handedness)
