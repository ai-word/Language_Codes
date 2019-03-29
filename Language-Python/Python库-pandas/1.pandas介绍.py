import pandas as pd
import numpy as np
# 创建一个序列
s = pd.Series([1,2,3,4,8,np.nan])
print(s)
print(s.dtype)

dates = pd.date_range("20191212",periods=6)
print(dates)

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['a','b','c','d'])
print(df)
#                    a         b         c         d
# 2019-12-12  0.580689  0.227857  0.341255  0.624844
# 2019-12-13  0.900691  0.770015  0.761280  0.419052
# 2019-12-14  0.512718  0.345403  0.364958  0.428675
# 2019-12-15  0.432096  0.479922  0.679457  0.131051
# 2019-12-16  0.163207  0.622022  0.678202  0.722188
# 2019-12-17  0.207933  0.895404  0.615309  0.791830

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11

df2 = pd.DataFrame(np.arange(12).reshape(3,4),index=['e','f','g'],columns=['a','b','c','d'])
print(df2)
print(df2.dtypes)
# 输出所有列的标序
print(df2.index)
# 打印所有列的名字
print(df2.columns)
# 值
print(df2.values)
# 打印该矩阵的描述 平均值。方差。
print(df2.describe())
# 矩阵转置
print(df2.T)
# 排序索引
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_index(axis=0,ascending=False))
# 排序value
print(df2.sort_values(by='a'))
