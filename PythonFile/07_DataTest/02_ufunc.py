import time
import math
import numpy as np

x = [i*0.001 for i in range(1000000)]
start = process_time()
for i,t in enumerate(x):
    x[i] = math.sin(t)

print("math.sin:",time.clock()- start)

x = [i * 0.001 for i in range(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print("numpy.sin",time.clock()- start)