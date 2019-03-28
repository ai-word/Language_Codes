#支持的格式，可以有三种：

#1. 带等于号的：
# coding=<encoding name>

#2. 最常见的，带冒号的（大多数编辑器都可以正确识别的）：
#!/usr/bin/python
# -*- coding: <encoding name> -*-

#3.vim的：
#!/usr/bin/python
# vim: set fileencoding=<encoding name> :


# 例子
# -*- coding: utf-8 -*-
import math
# 声明的好处：防止中文按照默认的ASCII码进行编码而出现乱码

