import numpy as np


a = np.arange(10).reshape(2,5)
print(a)
# 加法，每个元素一次相加

print(a + 10)
print(a ** 2)

c = 10 * np.sin(a)
print(c)
# 判断array有哪些值,打印小于3的值
print(c < 3)

l = np.arange(1,5).reshape(2,2)
m = np.arange(5,9).reshape(2,2)
print(l)
print(m)
# 矩阵乘法
# 逐个相乘
n = l * m
print(n)
# 矩阵乘法
n_dot = np.dot(l,m)
print(n_dot)
n_d = l.dot(m)
print(n_d)

# 2行4列矩阵0-1随机数字
rm = np.random.random((2,4))
print(rm)

# 最小值
print(np.min(rm))
# 和
print(np.sum(rm))
print(np.sum(n))

# 最大值
# 1每一行求值；0每一列求值
print(np.max(rm,axis=1))
print(np.max(rm,axis=0))



