import threading
import time
from threading import *
from time import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(0.3)
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(0.3)

t1 = hello()
t2 = hi()
t1.start()
sleep(0.1)
t2.start()
t1.join()
t2.join()

print("bye")


def add(a, b):
    for i in range(5):
        print(a+b)
        sleep(0.11)
def sub(a, b):
    for i in range(5):
        print(a-b)
        sleep(0.11)
t1 = threading.Thread(target=add,args=(5,10))
t2 = threading.Thread(target=sub,args=(10,5))

t1.start()
sleep(0.10)
t2.start()
t1.join()
t2.join()
print("multi tasking done")

