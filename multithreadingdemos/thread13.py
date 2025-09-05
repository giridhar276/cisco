# -*- coding: utf-8 -*-
"""
Write a pgm to create 3 daemon threads, and using the enumerate and join function, wait for the deamon threads to complete execution
"""
#current running thread is mai thread


import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


def uf():
    logging.debug('Starting')
    time.sleep(30)
    logging.debug('Exiting')
    
for i in range(3):   
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


#if your observre our understand was ew will be waiting for child threads to be exited:
#and we will exit
#there are threads which have exited even before we have join on thoese threads
# thread2 has exited and afer exiting we have mainthread to wait for thread 2
# and there is thread3 which is exited
#since threads are executed i parallel in one or other way there are chances
#that they might not get sync.
# the main program shoudl wait until all child threads to finish its executed

   