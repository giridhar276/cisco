

# create to create 5 threads to execute in parallel



import threading

def uf(num1,num2):
    """thread uf function"""
    print("numbers :{} {}".format(num1,num2))
    print("result  : {}".format(num1 + num2))
    
    
    
threads = []

for i in range(5):
    t = threading.Thread(target=uf , args=(2,1))
    threads.append(t)
    t.start()
    