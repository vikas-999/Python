'''
class demo:
    num = 10
    def display(self):
        print(demo.num)
class sample(demo):
    num=20
a = sample()
a.display()

class sample:
    num=20

class demo(sample):
    num = 10
    def __int__(self,a):
        self.a = a
    @classmethod
    def display(cls):
        print(cls.num)


a = demo()
a.display()
'''


class demo:
    num = 10
    def __init__(self, x):
        self.x = x
    def display(self):
        print(self.__class__.num)
        print(self.x)

class sample(demo):
    num = 20
a = sample(6)
a.display()
b= sample(10)
b.display()



