import time

def time_now_epoch_demo():
    print("Epoch seconds:", time.time())
    print("Human time:", time.ctime())

def time_local_gmt_demo():
    lt = time.localtime()
    gt = time.gmtime()
    print("Local:", lt)
    print("GMT  :", gt)

def time_strftime_demo():
    s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Formatted now:", s)

time_now_epoch_demo()
time_local_gmt_demo()
time_strftime_demo()
