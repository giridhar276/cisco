

## passing arguments to the thread


import threading

def uf(num1,num2):
    """thread uf function"""
    print("numbers :{} {}".format(num1,num2))
    print("result  : {}".format(num1 + num2))
    
    
t = threading.Thread(target=uf, args = (2,3))    
t.start()