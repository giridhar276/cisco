# -*- coding: utf-8 -*-
"""
Write a pgm where in a thread waits for a particular event indefinitely. 
once the event is set by the main thread, the thread stops waiting and resumes execution
"""

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')



def function_waiting_for_event(e):
    """wait for the event to be set before doing anything"""
    logging.debug('function waiting for event starting')
    event_is_set = e.wait()
    logging.debug('event set :{}'.format(event_is_set))
    
    
e = threading.Event()
t1 = threading.Thread(name = 'userfunctinwaitinforevent',
                      target=function_waiting_for_event,
                      args=(e,))


t1.start()

logging.debug('Waiting before calling event set()')
time.sleep(3)
# will set the event and notify all the other threads which are waiting to set
e.set()
logging.debug('Event is set')