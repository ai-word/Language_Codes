from multiprocessing import Pool
import os
import random
import time

def worker(num):
    for i in range(5):
        print("===pid=%d==num=%d="%(os.getpid(), num))
        time.sleep(1)

#3表示 进程池中对多有3个进程一起执行
pool = Pool(3)

for i in range(10):
    print("---%d---"%i)
    pool.apply(worker, (i,))#堵塞的方式


pool.close()#关闭进程池，相当于　不能够再次添加新任务了
pool.join()#主进程　创建／添加　任务后，主进程　默认不会等待进程池中的任务执行完后才结束
            #而是　当主进程的任务做完之后　立马结束，，，如果这个地方没join,会导致
            #进程池中的任务不会执行
