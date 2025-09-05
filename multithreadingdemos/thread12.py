# -*- coding: utf-8 -*-
"""
Write a pgm to check if the thread is still active and is the thread a daemon
"""

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


def uf():
    logging.debug('Starting')
    time.sleep(10)
    logging.debug('Exiting')
    
    
t= threading.Thread(name = 'daemonthread' , target=uf)


# main thread or main program which created this thread doesnt have to wait this thread
# daemon thread will be having its own indepent flow of execution
t.setDaemon(True)
t.start()
# 2 indicates hte period of time in seconds
# the main thread will wait for child thread for execution
# will wait for 2 seconds and resume execution
t.join(2)

print("t.isAlive()   :",t.is_alive())
print("t.isDaemon()  :",t.isDaemon())
time.sleep(30)
print('After 15 sec')
print("t.isAlive()   :",t.is_alive())
print("t.isDaemon()  :",t.isDaemon())
