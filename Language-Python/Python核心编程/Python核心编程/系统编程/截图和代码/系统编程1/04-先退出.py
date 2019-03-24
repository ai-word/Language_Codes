import os
import time

ret = os.fork()

if ret==0:
    print("----子进程1---")
    time.sleep(5)
    print("----子进程2---")
else:
    print("----父进程---")
    time.sleep(3)


print("----over---")
