# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

# 文件的重命名、删除
# 有些时候，需要对文件进行重命名、删除等一些操作，python的os模块中都有这么功能

# 文件重命名
# os模块中的rename()可以完成对文件的重命名操作
# rename(需要修改的文件名, 新的文件名)

import os
import os
# 文件夹的相关操作
# 实际开发中，有时需要用程序的方式对文件夹进行一定的操作，比如创建、删除等
#
# 就像对文件操作需要os模块一样，如果要操作文件夹，同样需要os模块


# 1.创建文件夹
# os.mkdir("liuyugang")

# 2.获取当前文件夹
w = os.getcwd()
print(w)

# 3. 改变默认目录
# os.chdir("../")

# 4.获取目录列表
print(os.listdir("./"))

# 5.删除文件夹
# os.rmdir("liuyugang")