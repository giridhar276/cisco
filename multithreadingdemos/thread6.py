

import threading
import time


def ug():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'exiting')
    
    
w = threading.Thread(target=ug)
w.start()