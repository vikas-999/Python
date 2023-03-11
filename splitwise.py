#abstraction
from abc import ABC, abstractmethod
#spliwise app example
'''
spitwise is an application, suppose if there is a person A who paied 3000 rupees for 3 people person B, person c
so those 3000 rupees will be split equally to all the 3 persons, in this case it will be split by 1000 ruppess each
person B and person C can also pay the amount and they can add the splits amoung each other
at any time they can clear there splits

'''
class split(ABC):
    @abstractmethod
    def splitbalance(self):
        pass
    @abstractmethod
    def split_a(self,amount,members):
        pass
    def split_pay(self,amount):
        pass
class splitwise(split):
    def __init__(self,balance = 1000):
        self.balance = balance
    def splitbalance(self):
        print("your current amount you have to settle is : ", self.balance)
    def split_a(self,amount,members):
        n = amount/members
        print("amount you have to pay is : ",self.balance)
        print(n, " is added to your balance")
        self.balance += n
        print("your current balance is : ",self.balance)
    def split_pay(self,amount):
        self.balance -= amount
        print("you paid : ", amount)
        print("your current balance to be paid is : ", self.balance)




c = splitwise()
c.split_a(100,5)
c.split_pay(500)








