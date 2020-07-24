import threading
import time
exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def  run(self):
        print('Start ' + self.name)
        print_time(self.name, self.counter, 3)
        print('Exiting ' + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1
thread1 = myThread(1, "Thread-1", 2)
thread2 = myThread(2, "Thread-2", 8)

thread1.start()      #start()方法通过调用run方法来启动线程
thread2.start()
thread1.join()       #jion()方法等等线程终止
thread2.join()
print("Exiting Main Thread")

