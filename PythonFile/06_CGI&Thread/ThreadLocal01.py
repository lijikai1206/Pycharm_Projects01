import threading

#创建全局ThreadLocal对象：
local_school = threading.local()

def process_student(name):
    #获取当前线程关联的student：
    std = local_school.student(name)
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_student, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_student, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
