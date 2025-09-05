
# program to create 5 threads which in turn each will print hello world

import threading


def uf():
    """thread of uf function"""
    print('hello world')
    return


threads = []

for i in range(5):
    t = threading.Thread(target=uf)
    #threads.append(t)
    t.start()
    