from threading import Thread
import threading
import time

def test1():
    #注意：
    #   1. 全局变量在多个线程中　共享，为了保证正确运行需要锁
    #   2. 非全局变量在每个线程中　各有一份，不会共享，当然了不需要加锁
    name = threading.current_thread().name
    print("----thread name is %s ----"%name)
    g_num = 100
    if name == "Thread-1": 
        g_num += 1
    else:
        time.sleep(2)
    print("--thread is %s----g_num=%d"%(name,g_num))

#def test2():
#    time.sleep(1)
#    g_num = 100
#    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1)
p2.start()

