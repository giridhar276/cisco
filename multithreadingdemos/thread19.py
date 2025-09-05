# -*- coding: utf-8 -*-
"""
 Write a pgm where in the main thread tries to acquire the lock twice in a sequential fashion
"""

# import threading

# lock = threading.Lock()

# print('First try  :',lock.acquire())

# print('Second try  :',lock.acquire())





# in the second statement we are trying to acquire the lock once again

import threading

lock = threading.RLock()

print('First try  :',lock.acquire())

print('Second try  :',lock.acquire(0))
