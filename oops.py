# oops
'''
class Demo:
    def __init__(self,x,y):
        self.x1 = x
        self.y1 = y
    def add(self):
        print(self.x1 + self.y1)
    def sub(self):
        print(self.x1 -self.y1)

d = Demo(2,3)
d.add()




class Employee:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def display(self):
        print(self.first)
        print(self.last)


e = Employee("Balavikas","sabbineni")
e1 = Employee("Juhitha","sabbineni")
e1.firstname = "sireesha"
e1.display()
e.display()

'''

class Demo:
        x =10
        y =20

print(Demo().x)

d = Demo()
d.x = 11
print(d.x)
Demo.x = 22
print(Demo.x)
d1 = Demo()
print(d1.x)

print(d.__dict__)
