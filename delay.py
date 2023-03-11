import time
"""
def delay(n):
    def o_delay(func):
        def i_delay(*args,**kwargs):
            print("wait for 3 sec")
            time.sleep(n)
            func(*args,**kwargs)
        return i_delay
    return o_delay
@delay(3)
def display(m):
    print(m)

display("hey sup?")


def wait(func):
    def i_wait(*args,**kwargs):
        print("wait for 3 sec the string is being reversed")
        time.sleep(3)
        func(*args,**kwargs)
    return i_wait

@wait
def rev_(m):
    print(m[::-1])
rev_("python")

def check(func):
    def i_check(*args,**kwargs):
        if isinstance(args,(str,list,tuple,dict)):
            print(args)
        print(type(func(*args)))
    return i_check
@check
def args_(n):
    print(n)
args_(1)
"""

def pos(func):
    def i_pos(*args,**kwargs):
        c=0
        for i in args:
            if i > 0:
                c+=1
        if c >=2:
            func(*args,**kwargs)
        else:
            print("its not possible with negative arguments")
    return i_pos

@pos
def add(a,b):
    print(a+b)



