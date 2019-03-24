class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge
    
    def eat(self):
        print("-----%s正在吃----"%self.name)


def run(self):
    print("-----%s正在跑----"%self.name)


p1 = Person("p1", 10)
p1.eat()
p1.run = run
p1.run()#虽然p1对象中 run属性已经指向了10行的函数,,,但是这句代码还不正确
        #因为run属性指向的函数 是后来添加的,几p1.run()的时候,并没有把p1当做第
        #1个参数,导致了第10行的函数调用的时候, 出现缺少参数的问题
