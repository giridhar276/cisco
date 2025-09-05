

'''
 Write a pgm to create a thread which is not dependent on the main thread (create a daemon thread)
'''

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


def uf():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
    
    
w= threading.Thread(name = 'non- daemon' , target=uf)
w.start()

############################

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


def uf():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
    
    
w= threading.Thread(name = 'daemonthread' , target=uf)



w.setDaemon(True)
w.start()


# main thread or main program which created this thread doesnt have to wait this thread
# daemon thread will be having its own indepent flow of execution



