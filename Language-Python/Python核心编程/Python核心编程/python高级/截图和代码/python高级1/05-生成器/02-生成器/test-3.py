def creatNum():
    print("------start----")
    a,b = 0,1
    for i in range(5):
        print("----1---")
        yield b
        print("----2---")
        a,b = b,a+b
        print("----3---")
    print("------stop----")

#创建了一个生成器对象
a = creatNum()

ret = a.__next__()
print(ret)

#注意:
#next(a)
#a.__next__()
#以上两种方式是一样的
