# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# for循环
name = 'dongGe'

for x in name:
    print('----')
    print(x)
# 带有break的循环示例如下:
name = 'dongGe'
for x in name:
    print('----')
    if x == 'g':
        break
    print(x)

# while 循环
x = 10
while x < 100:
    x = x + 1
    print(x)
    if x == 78:
        break


# 总结：
# break的作用：用来结束整个循环
x = 10
while x < 100:
    x = x + 1
    print(x)
    if x == 78:
        continue

# continue的作用：用来结束本次循环，紧接着执行下一次的循环
#
# 注意点
# break/continue只能用在循环中，除此以外不能单独使用
# break/continue在嵌套循环中，只对最近的一层循环起作用
