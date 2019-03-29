import pandas as pd
import numpy as np
dates = pd.date_range("20191212",periods=6)
print(dates)

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['A','B','C','D'])
print(df)
# 改变值
df.iloc[2,2] = 111
df.loc['20191212','A'] = 2222
df[df.A>1] = 900
print(df)
# 加一个空行
df['F'] = np.nan
d = pd.date_range('20191212',periods=6)
df["G"] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20191212',periods=6))
print(df)

