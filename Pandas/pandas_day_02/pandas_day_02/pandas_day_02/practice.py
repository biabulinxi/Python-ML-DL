import numpy as np
import pandas as pd
# 创建DataFrame
df = pd.DataFrame([['Snow','M',22],['Tyrion','M',32],['Sansa','F',18],['Arya','F',14]], columns=['name','gender','age'])
# print(df)
#选去多列，gender和age列
# print(df[['name','gender']])
# print(df.loc[:,['name','gender']])
# print(df.iloc[:,[0,1]])
# print(df.iloc[:,0:2])

#读取第1行到第2行的数据
# print(df[1:3])
# print(df.iloc[1:3])

#读取第1行和第3行，从第0列到第2列,不包括第二列
# print(df.iloc[[1,3],0:2])

#读取倒数第3行到倒数第1行的数据
# print(df[-3:-1])

#################################################
print('本节课内容')
df1=df.copy()
# print(df1)

# 修改 snow 的年龄为 25
# df1.loc[0,'age'] =25
# print(df1)
# df1.iloc[0,2] =25
# print(df1)
# # 去某个单值
# df1.at[0,'age'] = 25
# df1.iat[0,2] = 25

# 给上个例子学生加上score一列。分别为：80，98，67，90
df1['score'] = [89,85,90,78]
print(df1)

# 在gender后面加一列城市, 利用列表的insert方法
# index -- 对象 obj 需要插入的索引位置。
# obj -- 要插入列表中的对象
col_name = df1.columns.tolist()
col_name.insert(2,'city')
df1 = df1.reindex(columns=col_name)
df1['city'] = ['xian','beijng','chengdu','shenzhen']
print(df1)


# 给上个例子学生加上一行信息
#首先，要创建一个DataFrame。要注意，在这里需加入index属性，lisa F 北京 19 100
new = pd.DataFrame({'name':'lisa','gender':'F','city':'beijing','age':19,'score':100},index=[0])
#然后，开始插值。ignore_index=True,可以帮助忽略index，自动递增。
df1 = df1.append(new,ignore_index=True)
print(df1)


print('删除功能练习')
# 删除第0行
df2 = df1.drop(labels=0,axis=0)
print(df2)

# 删除第score列
df3 = df1.drop(labels='score',axis=1)
print(df3)
print(df1)

# 对score列排序,降序
df4 = df1.sort_values(by='score',ascending=False)
print(df4)

