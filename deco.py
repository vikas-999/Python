# using decorators
'''
def deco(func):
    def wrapper(*args, **kwargs):
        print("addition of two numbers is : ", end=" ")
        func(*args, **kwargs)
    return wrapper
'''
import time


class decor( ):
    def __init__(self,time):
        self.time = time
    def __call__(self, func):
        def wrapper(*args,**kwargs):
            time.sleep(self.time)
            print("good morning")
            func(*args,**kwargs)
        return wrapper


@decor(3)
def add(a ,b):
    print(a + b)

add(3, 30)

