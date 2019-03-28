# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

PI = 3.14
def get_sum(lst):
    """
    Sum the values in the list
    :param lst:
    :return:
    """
    total = 0
    for v in lst:
        total = total + v
    return total


def test():
    l = [1, 2, 3]
    assert (get_sum(l) == 6)
    print("test pass.")


if __name__ == '__main__': #单个模块测试时写法，该用法的作用是作为模块被导入时，改语句是不执行的；如果作为单个模块测试时，是执行的
    test()