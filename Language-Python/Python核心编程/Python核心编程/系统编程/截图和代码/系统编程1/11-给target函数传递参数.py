from multiprocessing import Process
import os

def test(num):
    print("pid=%d,ppid=%d,,,,num=%d"%(os.getpid(), os.getppid(), num))


p = Process(target=test, args=(100,))
p.start()
print("----main--pid=%d--"%os.getpid())
