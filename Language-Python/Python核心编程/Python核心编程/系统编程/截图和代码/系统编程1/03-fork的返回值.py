import os

ret = os.fork()
print(ret)
if ret>0:
    print("---父进程--%d-"%os.getpid())
else:
    print("---子进程---%d-%d-"%(os.getpid(),os.getppid()))

