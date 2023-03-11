import pandas as pd

class bank:
    bank_name = "us bank"
    branch = "st cloud"
    pin = 56301

    def __init__(self, cname, acc, balance):
        self.cname = cname
        self.acc = acc
        self.balance = balance
        self.st = list([[1, "-", "-", self.balance]])



    def display(self):
        print(f"{'='*40}\n"
              f"bank details\n{'-'*20}\n"
              f"bank name : {self.bank_name}\n"
              f"branch : {self.branch}\n"
              f"pin : {self.pin}\n\n"
              f"customer details\n{'-'*20}\n"
              f"customer name : {self.cname}\n"
              f"account number: {self.acc}\n"
              f"balance : {self.balance}\n"
              f"{'='*40}\n")
    def deposit(self,amount):
        self.amount = amount
        print(f"current balance : {self.balance}\n"
              f"deposit amount : {self.amount}")
        self.balance += self.amount
        print(f"total balance : {self.balance}\n")
        i = self.st[-1][0] + 1
        l = [[i, self.amount, "-", self.balance]]
        self.st+= l

    def withdraw(self,amount):
        self.amount = amount
        print(f"current balance : {self.balance}\n"
              f"withdrawal amount : {self.amount}")
        self.balance -= self.amount
        print(f"total balance : {self.balance}\n")
        i = self.st[-1][0] + 1
        l = [[i, "-", self.amount, self.balance]]
        self.st += l

    def transfer(self, cust, amount):
        self.amount = amount
        print(f"current balance : {self.balance}\n"
              f"transfer amount : {self.amount}")
        self.balance -= self.amount
        cust.balance += self.amount
        print(f"total balance : {self.balance}\n")
        i = self.st[-1][0] + 1
        l = [[i, "-", self.amount, self.balance]]
        self.st += l
        i1 = cust.st[-1][0] + 1
        l1 = [[i1, amount, "-", cust.balance]]
        cust.st += l1
    def statement(self):
        print(f"{self.cname} statement")
        print(f"s.no  deposite   withdraw   total")
        for i in self.st:
            for j in i:
                print(j,end="        ")
            print(end="\n")



c1 = bank("vikas", "ST56301", 500)
c2 = bank("rohit", "ST33056", 2000)

print(c1.display(), c1.deposit(250), c1.deposit(100), c1.withdraw(70), c1.transfer(c2, 5), c1.statement(), end="\n")
print(c2.statement())
'''

bank.bank_name = "buffa"
print(bank.bank_name)
c1 = bank("vikas", "ST56301", 500)
c2 = bank("rohit", "ST33056", 2000)
print(c2.bank_name)
'''