import threading, multiprocessing
#这是一个死循环啊！
def loop():
    x = 0
    while True:
        x  = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()