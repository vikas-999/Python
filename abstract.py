from abc import ABC, abstractmethod
class base(ABC):
    @abstractmethod
    def spam(self):
        pass
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def act(self):
        pass
class derived(base):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def display(self):
        print(self.a + self.b)
    def spam(self):
        print("you cant use this its just a spam")
    def act(self):
        print(self.a, self.b)

a = derived(2,3)
a.act()
a.display()