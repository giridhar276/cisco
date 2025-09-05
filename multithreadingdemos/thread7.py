



import threading
import time


def ug():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'exiting')
    

def serviceFunction():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'exiting')    
    
    

t = threading.Thread(name = 'serviceFunction', target=serviceFunction)
w = threading.Thread(name = 'ug', target=ug)
w2 = threading.Thread(target=ug)

w.start()
w2.start()
t.start()