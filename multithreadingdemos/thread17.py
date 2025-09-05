# -*- coding: utf-8 -*-
"""
 Write a pgm where in a thread waits for a particular event for a particular period of time.
 once the event is set by the main thread, the thread stops waiting and resumes execution
"""

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')



def user_function_waiting_for_event_timeout(e,t):
    """wait for the event to be set before doing anything"""
    logging.debug('function waiting for event starting')
    event_is_set = e.wait(t)
    logging.debug('event set :{}'.format(event_is_set))
    if event_is_set :
        logging.debug('Processing event')
    else:
        logging.debug('doing other work')
    
e = threading.Event()
t2 = threading.Thread(name = 'non block wait for event',
                      target=user_function_waiting_for_event_timeout,
                      args=(e,2))


t2.start()

logging.debug('Waiting before calling event set()')
time.sleep(5)
# will set the event and notify all the other threads which are waiting to set
e.set()
logging.debug('Event is set')