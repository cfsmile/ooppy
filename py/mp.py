#! /usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process, cpu_count
import time
import os
from threading import Thread

class MuchCPU(Process):
# class MuchCPU(Thread):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass

if __name__ == '__main__':        
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()

    for p in procs:
        p.start()
    
    for p in procs:
        p.join()
    
    print("work took {} seconds".format(time.time() - t))



# 4300
# 4301
# 4302
# 4303
# 4305
# 4304
# 4306
# 4307
# work took 8.239726066589355 seconds


# 4351
# 4351
# 4351
# 4351
# 4351
# 4351
# 4351
# 4351
# work took 33.17213773727417 seconds
