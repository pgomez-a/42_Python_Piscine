import time
import os

def ft_progress(lst):
    init_time = time.time()
    iter_time = time.time()
    bar = ""
    for item in lst:
        os.system("clear")
        print("ETA: {:.2f}s".format(time.time() - init_time), end=" ")
        print("[{:.2f}%]".format((item / len(lst)) * 100), end=" ")
        if int((item / len(lst)) * 10) != len(bar):
            bar += "="
        print("[{: <10}]".format(bar + ">"), end=" ")
        print("{}/{}".format(item, len(lst)), end=" ")
        print("| elapsed time {:.2f}s".format(time.time() - iter_time))
        iter_time = time.time()
        yield item

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
