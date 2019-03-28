# -*— coding utf-8 -*-

# 兼容python3的print写法
from __future__ import print_function
# 兼容python3的编码处理
from __future__ import unicode_literals

s = 'hello world'
print(s[0]) #h
print(s[-2]) #l

# 切片 来从序列中提取出想要的子序列，其用法：
# 语法：var[lower:upper:step]
# 解释：step:步长
print(s[-2:]) #ld
print(s[0::2])#hlowrd
print(s[::]) #hello world