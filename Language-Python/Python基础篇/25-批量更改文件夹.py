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
# coding=utf-8

# 批量在文件名前加前缀

import os

funFlag = 1  # 1表示添加标志  2表示删除标志

folderName = './renameDir/'

# 获取指定路径的所有文件名字
dirList = os.listdir(folderName)
# 遍历输出所有文件名字
for name in dirList:
    print(name)

    if funFlag == 1:
        newName = '[东哥出品]-' + name
    elif funFlag == 2:
        num = len('[东哥出品]-')
        newName = name[num:]
    print(newName)

    os.rename(folderName + name, folderName + newName)