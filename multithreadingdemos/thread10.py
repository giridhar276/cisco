# -*- coding: utf-8 -*-
"""
Write a pgm to do the following:
     - Create a daemon thread
     - From the main thread function, wait for a stipulated period to the daemon
     thread to complete execution
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
    
    
t= threading.Thread(name = 'daemonthread' , target=uf)


# main thread or main program which created this thread doesnt have to wait this thread
# daemon thread will be having its own indepent flow of execution
t.setDaemon(True)
t.start()
t.join()