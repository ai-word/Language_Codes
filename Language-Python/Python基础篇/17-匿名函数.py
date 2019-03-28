# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# 匿名函数：用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。
# lambda函数的语法只包含一个语句，如下
# lambda [arg1[, arg2, .....argn]]: expression

# 例子：
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))


# 应用场合
# 函数作为参数传递
def fun(a, b, opt):
    print("a =", a)
    print("b =", b)
    print("result =", opt(a, b))

# 调用

fun(1, 2, lambda x, y: x + y)


# 排序
stus = [
    {"name":"zhangsan", "age":18},
    {"name":"lisi", "age":19},
    {"name":"wangwu", "age":17}
]
# 按name排序：
stus.sort(key = lambda x:x['name'])
print(stus)

# 按age排序：
stus.sort(key = lambda x:x['age'])
print(stus)