import pandas as pd
import numpy as np
dates = pd.date_range("20191212",periods=6)

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['A','B','C','D'])
# 改变值
df.iloc[2,2] = 111
df.loc['20191212','A'] = 2222
df[df.A>1] = 900
# 加一个空行
df['F'] = np.nan
d = pd.date_range('20191212',periods=6)
df["G"] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20191212',periods=6))
print(df)
# 放弃掉某个数据
print(df.dropna(axis=1))
# 只有出现none 就丢掉 how='any','all'
print(df.dropna(axis=0,how='any'))
# 全部等于none就丢掉
print(df.dropna(axis=0,how='all'))

# 遇到non就填入数字
print(df.fillna(value=0))

# 是non就填入
print(np.any(df.isnull())==True)

