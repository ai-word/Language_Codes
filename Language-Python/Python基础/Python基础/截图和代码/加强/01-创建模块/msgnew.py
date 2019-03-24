#如果导入这个模块的方式是 from 模块名 import * ,那么仅仅会导入__all__的列表中包含的名字
__all__ = ["test1","Test"]

def test1():
    print("----test-1-----")

def test2():
    print("----test-2-----")

num = 100

class Test(object):
    pass
