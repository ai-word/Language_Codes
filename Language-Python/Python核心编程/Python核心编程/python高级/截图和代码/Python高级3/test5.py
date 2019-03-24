class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    #属性访问时拦截器，打log
    def __getattribute__(self,obj):
        print("====1>%s"%obj)
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:   #测试时注释掉这2行，将找不到subject2
            temp = object.__getattribute__(self,obj)
            print("====2>%s"%str(temp))
            # return temp

    def show(self):
        print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)

s.show()
#1. 先获取show属性对应的结果，，，，应该是一个方法
#2. 方法()

# import types
# p1.eat = types.MethodType(eat, p1)
