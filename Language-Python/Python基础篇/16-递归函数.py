# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
# 递归函数：如果一个函数在内部不调用其它的函数，而是自己本身的话，这个函数就是递归函数。
# 举个例子，我们来计算阶乘 n! = 1 * 2 * 3 * ... * n

def calNum(num):
    if num >= 1:
        result = num * calNum(num - 1)
    else:
        result = 1
    return result

# 调用：
res = calNum(10)
print(res)