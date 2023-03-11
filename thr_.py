import threading
def add(a):
    print("add",a*a)
def sub(b):
    print("sub",b*b*b)

t1 = threading.Thread(target=add,args=(10,))
t2 = threading.Thread(target=sub,args=(11,))

t1.start()
t2.start()

