import numpy as np
a = np.arange(12).reshape((3,4))
print(a)
# axis=1 列分割
print(np.split(a,2,axis=1))
#  axis=0 行分割
print(np.split(a,3,axis=0))

# 不等量分割
print(np.array_split(a,3,axis=1))

# axis=1 列分割
print(np.vsplit(a,3))
#  axis=0 行分割
print(np.hsplit(a,2))