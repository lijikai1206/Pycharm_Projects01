import time

def clock():
    while True:
        cur_time = time.localtime()
        t_hms = cur_time[3:6]
        print("%02d:%02d:%02d" % t_hms, end='\r')
        time.sleep(2)

clock()