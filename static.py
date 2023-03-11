#static
class sample:
    @staticmethod
    def spam(msg):
        print(msg)
c = sample()
c.spam("helloworld")

#2nd one
class demo:
    @staticmethod
    def display():
        print("this is the method inside demo")
c1 = demo()
c1.display()

class sample1():
    @staticmethod
    def add(a,b):
        print(a+b)
a =sample1()
a.add(2,3)

#classmethod
class samclass():
    company = "scsu"
    @classmethod
    def name(cls,company):
        cls.company=company
o1 = samclass()
o2 = samclass()
o1.name("st. cloud")
print(o2.company)






#call
class log:
    def __call__(self,n):
        if n%2 == 0:
            print(f"{n} is even")
        else:
            print(f"{n} is odd")
l = log()
l(2)

#2nd one
class out:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("the addition of two numbers : ", end="")
            func(*args, **kwargs)
        return wrapper
@out()
def add(a,b):
    print(a+b)
add(10,10)










