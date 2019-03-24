import os

os.fork()
os.fork()
#下面是fork炸弹,不相信你可以执行下看看
while True:
    os.fork()


print("----1---")
