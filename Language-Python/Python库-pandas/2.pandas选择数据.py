import pandas as pd
import numpy as np
dates = pd.date_range("20191212",periods=6)
print(dates)

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['A','B','C','D'])
print(df)
print(df['A'])
# 数据选择
print(df.loc['20191212'])
print(df.loc['20191212',['A','B']])

# 位置选择location
print(df.iloc[3])
# 第三行第一位
print(df.iloc[3,1])
print(df.iloc[[1,2,4],1:3])

# 两者结合筛选
print(df.ix[:3,['A','B']])

# bool index
print(df)
print(df[df.A>0.5])

