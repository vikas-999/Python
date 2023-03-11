class demo:
    def __init__(self, a):
        self.a = a

    def display(self):
        print("demo display")
class sample(demo):
    def __init__(self, b, a):
        self.b = b
        super().__init__(a)
    def display(self):
        print("sample display")
        print(self.a + self.b)
        super().display()
    def spam(self):
        print("spam")
a = sample(5, 4)
a.display()

