# coding:utf-8
class Bar(object):
    pass


class Foo(object):
    """"""

    def __init__(self):
        self.itcast = 10


    def __getattr__(self, item):
        print item,
        # hello_world
        return self

    def __getattribute__(self, item):
        return self.itcast
        # self.__getattribute__("itcast")

    def __str__(self):
        return ""


# obj = Foo()
# "think" obj.think
# obj.different

# print(Foo().think.different.itcast)
print(Foo().think)
