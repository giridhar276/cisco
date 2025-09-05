# -*- coding: utf-8 -*-
"""
Write a pgm which creates 2 threads which does the following with out conflict:
    Acquire the lock, increment the counter value and release the lock.
"""

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


class Counter:
    def __init__(self,start = 0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()
        
        
def userfunction(c):
    logging.debug('starting')
    time.sleep(3)
    c.increment()
    logging.debug('Exiting')
    
counter= Counter()
for i in range(2):
    t = threading.Thread(target=userfunction,args=(counter,))
    t.start()
    
logging.debug('waiting for userfunction threads')
main_thread  = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
    
    
        