# -*- coding: utf-8 -*-
"""
Write a pgm to create a daemon thread,
and using the enumerate and join function, wait for the daemon thread to complete execution
"""


import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


def uf():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
    
    
t= threading.Thread(target=uf)
t.setDaemon(True)
t.start()


main_thread = threading.currentThread()
## threading.enumerate() : get all the list of threads which are running
for t in threading.enumerate():
    if t is main_thread :
        continue
    logging.debug("joining %s", t.getName())
    t.join()
