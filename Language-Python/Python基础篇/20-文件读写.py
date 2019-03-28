# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# 写数据(write)
f = open('test.txt', 'w')
f.write('hello world, i am here!')
f.close()
# 注意：
# 如果文件不存在那么创建，如果存在那么就先清空，然后写入数据

# 读数据(read)
# 使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据
f = open('test.txt', 'r')
content = f.read(5)
print(content)
print("-"*30)
content = f.read()
print(content)
f.close()

# 注意：
# 如果open是打开一个文件，那么可以不用谢打开的模式，即只写 open('test.txt')
# 如果使用读了多次，那么后面读取的数据是从上次读完后的位置开始的

# 读数据（readlines）
# 就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
f = open('test.txt', 'r')
content = f.readlines()
print(type(content))
i=1
for temp in content:
    print("%d:%s"%(i, temp))
    i+=1
f.close()

# 读数据（readline）
f = open('test.txt', 'r')

content = f.readline()
print("1:%s"%content)

content = f.readline()
print("2:%s"%content)

f.close()