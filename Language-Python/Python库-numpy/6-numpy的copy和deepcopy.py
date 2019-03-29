import numpy as np
a = np.arange(4)
b = a.copy()
a[0] = 11
print(a)
print(b is a)
print(b)
# copy功能
e = a.copy()
print(e)