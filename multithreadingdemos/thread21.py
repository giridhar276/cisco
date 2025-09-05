# -*- coding: utf-8 -*-
"""
Write a pgm where two consumer threads wait on the producer thread to notify them about the availability of the resource
"""
import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


def consumer_thread(cond):
    """ wait for the condition and use the resource"""
    logging.debug('Starting consumer_thread thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer thread')
        
        
def producer_thread(cond):
    """set up the resource to be used by consumer thread"""
    logging.debug('Starting producer_thread thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()
        
        
condition = threading.Condition()

c1=threading.Thread(name = 'c1', target=consumer_thread,args=(condition,))
c2=threading.Thread(name = 'c2', target=consumer_thread,args=(condition,))
p=threading.Thread(name = 'p', target=producer_thread,args=(condition,))

c1.start()
c2.start()
p.start()