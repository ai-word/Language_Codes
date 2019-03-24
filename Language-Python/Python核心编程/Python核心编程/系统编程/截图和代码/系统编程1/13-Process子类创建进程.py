from multiprocessing import Process
import time

class MyNewProcess(Process):
    def run(self):
        while True:
            print("---1----")
            time.sleep(1)


p = MyNewProcess()
p.start()

while True:
    print("---main----")
    time.sleep(1)

