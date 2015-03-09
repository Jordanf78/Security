#!/usr/bin/env python
# Since orginal code running a slow!

import time
def timeSeconds(secondsCount):
    
    start = time.time()
    time.clock()
    ellapsed = 0
    while ellapsed < secondsCount:
        ellapsed = time.time() - start
        print("Time: %f, seconds: %02d" % (time.clock() , ellapsed))  
        time.sleep(1)
        
timeSeconds(50) 
