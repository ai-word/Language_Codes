# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
# 事实上，根据函数参数的多少，map 可以接受多组序列，
# 将其对应的元素作为参数传入函数：
def add(a, b):
    return a + b

a = (2 , 3 , 4)


b = [10, 11, 15]
print(map(add, a, b))  # [12, 14, 19]
