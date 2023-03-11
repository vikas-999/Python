'''
import _thread
import time
def square(n):
    for i in n:
        print("square : ",i*i)
        time.sleep(0.3)
def cube(n):
    for i in n:
        print("cube : ",i*i*i)
        time.sleep(0.3)
a = [11,12,13,14,15]
square(a)
cube(a)
'''
import threading
import time
def square(n):
    for i in n:
        print(f"square of {i} : ",i*i)
        time.sleep(0.3)
def cube(n):
    for i in n:
        print(f"cube of {i} : ",i*i*i)
        time.sleep(0.3)
a = [11,12,13]
t1 = threading.Thread(target=square, args=(a,))
t2 = threading.Thread(target=cube, args=(a,))
t1.start()
time.sleep(0.2)
t2.start()
t1.join()
t2.join()
print("done")
'''
from threading import *
import time
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            time.sleep(0.3)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            time.sleep(0.3)

a = hello()
b = hi()

a.start()
time.sleep(0.1)
b.start()

a.join()
b.join()

print("bye")
'''

