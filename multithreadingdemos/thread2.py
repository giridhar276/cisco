# program to create a thread which will print 'hello world'

import threading



def uf():
    """thread uf function"""
    print("hello world")
    return


threads = []
t = threading.Thread(target = uf)
threads.append(t)
t.start()
