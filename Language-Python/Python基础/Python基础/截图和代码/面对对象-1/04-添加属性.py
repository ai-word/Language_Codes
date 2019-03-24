class Cat:
    #属性

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

#创建一个对象
tom = Cat()

#调用tom指向的对象中的 方法
tom.eat()
tom.drink()

tom.name = "汤姆"
tom.age = 40
