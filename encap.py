#encapsulation is one of the oops principle
#for encapsulation we have public, protected(_), private(__) specifiers
#public specifier are normal, like we use regulary
class Name:
    def __init__(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary
    def display(self):
        print(f"employee name is {self.emp_name} & his salary is {self.salary}")

a = Name("vikas", 10.33)
a.display()

class name:
    def __init__(self, emp_name, salary):
        self._emp_name = emp_name
        self._salary = salary
    def display(self):
        print(f"employee name is {self._emp_name} & his salary is {self._salary}")

a = name("vikas", 10.33)
a.display()

class peru:
    def __init__(self, emp_name, salary):
        self.__emp_name = emp_name
        self.__salary = salary
    def display(self):
        print(f"employee name is {self.__emp_name} & his salary is {self.__salary}")

a = peru("vikas", 10.33)
a.display()
print(a.__dict__)