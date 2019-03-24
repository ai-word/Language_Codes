class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


laowang = Person("老王", 10000)
print(laowang.name)
print(laowang.age)
laowang.addr = "北京...."
print(laowang.addr)


laozhao = Person("老赵", 18)
#print(laozhao.addr)

Person.num = 100
print(laowang.num)
print(laozhao.num)
