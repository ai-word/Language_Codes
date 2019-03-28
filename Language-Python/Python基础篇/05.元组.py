# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
# Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。
a = (10, 11, 12, 13, 14)
print(a)

# 可以索引，切片：
c = a[0]
print(c)

c = a[1:3]
print(c)  # (11, 12)

# 单个元素的元组生成
# 采用下列方式定义只有一个元素的元组：
a = (10,)
print(a)
print(type(a))  # <type 'tuple'>

a = [1, 2, 3]
b = tuple(a)
print(b)  # (1, 2, 3)

# 由于元组是不可变的，所以只能有一些不可变的方法，
# 例如计算元素个数 count 和元素位置 index ，用法与列表一样。
c = a.count(1)
print(c)  # 1

c = a.index(3)
print(c)  # 索引位置为：2