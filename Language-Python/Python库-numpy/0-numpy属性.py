import numpy as np
# 导入numpy
# 很多其他科学计算的第三方库都是以Numpy为基础建立的。
# Numpy的一个重要特性是它的数组计算。
# 使用前一定要先导入 Numpy 包，导入的方法有以下几种：
# import numpy
# import numpy as np
# from numpy import *
# from numpy import array, sin
arr = [[1,2,3],[4,5,6]]
# 列表转矩阵
array = np.array(arr)
print(array)
# 矩阵维度
print(array.ndim)
# 矩阵行列
print(array.shape)
# 矩阵元素个数
print(array.size)