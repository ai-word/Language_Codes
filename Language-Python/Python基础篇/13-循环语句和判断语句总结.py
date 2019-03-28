# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# if往往用来对条件是否满足进行判断
# if有4中基本的使用方法：

# 基本方法
#     if 条件:
#         满足时做的事情
# 满足与否执行不同的事情
#     if 条件:
#         满足时做的事情
#     else:
#         不满足时做的事情


# 多个条件的判断
    # if 条件:
    #     满足时做的事情
    # elif 条件2:
    #     满足条件2时做的事情
    # elif 条件3:
    #     满足条件3时做的事情
    # else:
    #     条件都不满足时做的事情


# 嵌套
#     if 条件:
#         满足时做的事情
#         这里还可以放入其他任何形式的if判断语句

# while循环一般通过数值是否满足来确定循环的条件
i = 0
while i<10:
    print("hello")
    i+=1

# for循环一般是对能保存多个数据的变量，进行便利
name = 'dongGe'
for x in name:
    print(x)

# if、while、for等其他语句可以随意组合，这样往往就完成了复杂的功能