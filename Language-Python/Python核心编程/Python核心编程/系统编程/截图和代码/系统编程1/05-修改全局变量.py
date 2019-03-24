import os
import time

g_num = 100

ret = os.fork()
if ret == 0:
    print("----process-1----")
    g_num += 1
    print("---process-1 g_num=%d---"%g_num)
else:
    time.sleep(3)
    print("----process-2----")
    print("---process-2 g_num=%d---"%g_num)

#想要完成进程间的数据共享,需要一些方法:命名管道/无名管道/共享内存/消息队列/网络等
