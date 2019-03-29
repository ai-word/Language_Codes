import numpy as np
# 创建一个指定类型的矩阵
a = np.array([2,3,4],dtype=np.float)
print(a)
b = np.array([[1,2,3],[4,5,6]],dtype=np.int)
print(b)
# 全部为0的矩阵
z = np.zeros((3,4))
print(z)
# 全部为1的矩阵
one = np.ones((3,4),dtype=int)
print(one)
# 全部为空的矩阵
em = np.empty((3,4),dtype=int)
print(em)

# 生成一个10-20范围内的步长为2的矩阵
s = np.arange(10,20,2)
print(s)

# 3行4列的矩阵
s1 = np.arange(100).reshape(10,10)
print(s1)

# 生成1到10 20段的数列
l = np.linspace(1,10,20).reshape(4,5)
print(l)