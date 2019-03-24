def func(functionName):
    print("---func---1---")
    def func_in(a, b):#如果a,b 没有定义,那么会导致16行的调用失败
        print("---func_in---1---")
        functionName(a, b)#如果没有把a,b当做实参进行传递,那么会导致调用12行的函数失败
        print("---func_in---2---")

    print("---func---2---")
    return func_in

@func
def test(a, b):
    print("----test-a=%d,b=%d---"%(a,b))


test(11,22)
