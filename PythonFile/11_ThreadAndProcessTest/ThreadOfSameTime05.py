import threading

x = 0
def increment_global():
    global x
    x += 1
def taslofThread(lock):
    for _ in range(50000):
        lock.acquire()                #acquire()方法用于获取，即阻止锁定。默认参数为True。
        increment_global()
        lock.release()               #release()方法用于释放锁。
def main():
    global x
    x = 0

    lock = threading.Lock()
    t1 = threading.Thread(target= taslofThread, args=(lock,))
    t2 = threading.Thread(target= taslofThread, args=(lock,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i  in range(5):
        main()
        print("x = {1} after Iteration {0}".format(i, x))
