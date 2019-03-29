import numpy as np
a = np.arange(3)
b = np.arange(3,6)

# 上下合并
c = np.vstack((a,b))
print(c)
# 左右合并
d = np.hstack((a,b))
print(d)
print(d.shape)
#增加列
print(a[np.newaxis,:])
# 增加行
print(a[:,np.newaxis])

# 多个array合并 axis=0 上下方向 axis=1 左右方向
e = np.concatenate((a,a,a,a,a),axis=0)
print(e)