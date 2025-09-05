# -*- coding: utf-8 -*-
"""
What is the advantage of using a with statement to acquire a lock in a thread.
"""

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')




def thread_using_with(lock):
    with lock:
        logging.debug('Lock acquired via with')
        
        
def thread_not_using_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acqured directly')
    finally:
        lock.release()
        
lock = threading.Lock()
w= threading.Thread(target=thread_using_with , args = (lock,))

nw= threading.Thread(target=thread_not_using_with , args = (lock,))


w.start()

nw.start()