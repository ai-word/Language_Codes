# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

oldFileName = input("请输入要拷贝的文件名字:")

oldFile = open(oldFileName,'r')

# 如果打开文件
if oldFile:
    # 提取文件的后缀
    fileFlagNum = oldFileName.rfind('.')
    if fileFlagNum > 0:
        fileFlag = oldFileName[fileFlagNum:]
    # 组织新的文件名字
    newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
    # 创建新文件
    newFile = open(newFileName, 'w')
    # 把旧文件中的数据，一行一行的进行复制到新文件中
    for lineContent in oldFile.readlines():
        newFile.write(lineContent)
    # 关闭文件
    oldFile.close()
    newFile.close()