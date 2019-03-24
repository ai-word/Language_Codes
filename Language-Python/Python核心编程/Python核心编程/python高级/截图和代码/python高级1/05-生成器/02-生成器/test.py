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

for num in a:
    print(num)


