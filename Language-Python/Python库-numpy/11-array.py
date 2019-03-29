# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import tracemalloc #性能检测工具

# 　　在上面的代码中，用到了pytracemalloc几个核心的API：
# 　　start(nframe: int=1)　　
# 　　　　pytracemalloc的一大好处就是可以随时启停，start函数即开始追踪内存分配，相应的stop会停止追踪。start函数有一个参数，nframes : 内存分配时记录的栈的深度，这个值越大，pytracemalloc本身消耗的内存越多，在计算cumulative数据的时候有用。
#
# 　　get_traced_memory()
# 　　　　返回值是拥有两个元素的tuple，第一个元素是当前分配的内存，第二个元素是自内存追踪启动以来的内存峰值。
#
# 　　take_snapshot()　　　　
# 　　　　返回当前内存分配快照，返回值是Snapshot对象，该对象可以按照单个文件、单行、单个调用栈统计内存分配情况　
# 　　　
tracemalloc.start(10)
time1 = tracemalloc.take_snapshot()

import  numpy as np

# 给数组每个元素加1
a = [1,2,3,4]
# print(a+1) #报错

# 使用numpy.array创建数组
arr = np.array(a)
arr1 = arr + 1
print(arr1) #[2,3,4,5,6]

# 两个数组相加
res = arr + arr1
print(res)

# 对应元素相乘
print(arr * arr)

# 提取数组中的元素
# 提取第一个
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr2[0])

# 提取前两个元素
print(arr2[:2])

# 最后两个元素
print(arr2[-2:])

# 相加
print(arr2[:2]+arr2[-2:])
# 修改数组形状
# 查看array的形状：
s = arr2.shape
print(s)
arr3 = arr2.reshape(2,5)
print(arr3)

# 多维数组
# a 现在变成了一个二维的数组，可以进行加法：
# 乘法仍然是对应元素的乘积，并不是按照矩阵乘法来计算：
print(arr3*arr3)


