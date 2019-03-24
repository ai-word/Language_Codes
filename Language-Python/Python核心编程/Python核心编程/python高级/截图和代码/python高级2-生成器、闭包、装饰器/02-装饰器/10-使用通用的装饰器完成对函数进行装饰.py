def func(functionName):
    def func_in(*args, **kwargs):
        print("-----记录日志-----")
        ret = functionName(*args, **kwargs)
        return ret

    return func_in

@func
def test():
    print("----test----")
    return "haha"

@func
def test2():
    print("----test2---")

@func
def test3(a):
    print("-----test3--a=%d--"%a)

ret = test()
print("test return value is %s"%ret)

a = test2()
print("test2 return value is %s"%a)


test3(11)
