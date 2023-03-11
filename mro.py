'''
class Demo:
    def display(self):
        print("demo display")
class spam:
    def show(self):
        print("spam show")
    def display(self):
        print("spam display")

class sample(spam, Demo):
    def show(self):
        print("sample show")
    def display(self):
        print("sample display")

c = sample()
c.display()


class Demo:
    def display(self):
        print("demo display")
class spam(Demo):
    def show(self):
        print("spam show")
    def display(self):
        print("spam display")
        super().display()
c = spam()
c.display()


class cons1:
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def display(self):
        print(self.a,self.b)
class cons2(cons1):
    def __init__(self, x,a,b):
        self.x=x
        super().__init__(a,b)
    def show(self):
        print(self.x)

a = cons2(3,10,11)
a.display()
a.show()


class sample:
    num = 12
    def display(self):
        print(sample.num)
a = sample()
a.display()

class sample:
    num = 12
    def __int__(self, a):
        self.a = a
    @classmethod
    def display(cls):
        print(cls.num)
        print(self.a)

a = sample()
a.display()
'''
class sample:
    __a = 10
    __b = 20
    def add(self):
        print(self.__a+self.__b)

obj = sample()
obj.a