# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
# 事实上，根据函数参数的多少，map 可以接受多组序列，
# 将其对应的元素作为参数传入函数：
# 1.函数定义
# del 函数名():
#    代码块

# demo:
# def prints():
#     print("hello, world")

# 2.函数调用
# prints()

# 3.带参数函数
def add2num(a, b):
    c = a + b
    print(c)

def add2num(a, b):
    c = a + b
    print(a,b)
add2num(11, 22)  # 调用带有参数的函数时，需要在小括号中，传递数据

# 定义时小括号中的参数，用来接收参数用的，称为 “形参”
# 调用时小括号中的参数，用来传递给函数用的，称为 “实参”

# 4.函数返回值
def add2num(a, b):
    c = a + b
    return c
# 保存函数的返回值示例如下:
 #定义函数
    def add2num(a, b):
        return a+b

    #调用函数，顺便保存函数的返回值
    result = add2num(100,98)
    #因为result已经保存了add2num的返回值，所以接下来就可以使用了
    print(result)