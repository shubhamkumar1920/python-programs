# list vs generator
# memory usage,time
# when to use list,when to use generator
import time

t1 = time.time()
g =(i**2 for i in range(10000000))
print(time.time() - t1)