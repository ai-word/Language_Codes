import numpy as np


a = np.arange(12, 0,-1).reshape(3 , 4)
print(a)
# 计算最小值的索引
print(np.argmin(a))
# 计算最大值的索引
print(np.argmax(a))
# 计算整个矩阵的平均值
print(np.mean(a))
# 计算整个矩阵的行平均值
print(np.mean(a,axis=1))

# 计算整个矩阵的列平均值
print(np.mean(a,axis=0))

# 计算整个矩阵的中位数
print(np.median(a))

# 累加值
print(np.cumsum(a))
# 不是0的数
print(np.nonzero(a))
# 进行排序
print(np.sort(a))
# 矩阵的反向,行变列，列变行
print(np.transpose(a))
print(a.T)

# 所有小于5的数等于5，大于10 的数等于10
print(np.clip(a,5,10))
