# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# 获取当前读写的位置
# 在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取

# 打开一个已经存在的文件
f = open("test.txt", "r")
str = f.read(3)
print("读取的数据是 : ", str)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)

str = f.read(3)
print("读取的数据是 : ", str)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
f.close()

# 结果
# 读取的数据是 :  hel
# 当前文件位置 :  3
# 读取的数据是 :  lo
# 当前文件位置 :  6

# 定位到某个位置
# 如果在读写文件的过程中，需要从另外一个位置进行操作的话，可以使用seek()
#
# seek(offset, from)有2个参数
# offset:偏移量
# from:方向
# 0:表示文件开头
# 1:表示当前位置
# 2:表示文件末尾
# demo:把位置设置为：从文件开头，偏移5个字节

# 打开一个已经存在的文件
f = open("test.txt", "r")
str = f.read(30)
print("读取的数据是 : ", str)

# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
# 重新设置位置
f.seek(5, 0)
# 查找当前位置
position = f.tell()
print("当前文件位置 : ", position)
f.close()

# 结果：
# 读取的数据是 :  hello world, i am here!hello w
# 当前文件位置 :  30
# 当前文件位置 :  5
