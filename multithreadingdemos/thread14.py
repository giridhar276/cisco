# -*- coding: utf-8 -*-
"""
Write a pgm to override the run() function of thread
"""


import threading
import logging


logging.basicConfig(level = logging.DEBUG ,
                    format = '(%(threadName) -10s) - %(message)s')


class SubThread(threading.Thread):
    
    def run(self):
        logging.debug('starting')
        logging.debug('exiting')
        return
    
t = SubThread()
t.start()