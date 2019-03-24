from threading import Thread
import time

g_num = 0
g_flag = 1

def test1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(1000000):
            g_num += 1

        g_flag = 0

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    #轮询
    while True:
        if g_flag != 1:
            for i in range(1000000):
                g_num += 1
            break

    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()

#time.sleep(3) #取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)
