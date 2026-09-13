'''Encapsulation = Data ko protect karna + control access dena

Simple words:

Variables ko direct access se hide karna aur unko use karne ke liye methods provide karna.

Isse data safe rehta hai aur galat change hone se bachta hai.'''

class Student:
    def marks(self,number):
        self.__number=number
        return number
    def show(self):
        return self.__number
s=Student()
print(s.marks(30))
print(s.show())
print(s.__number)#error /can't access directly

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.amount=amount
        self.__balance+=self.amount
        return self.__balance
    def withdraw(self,amount):
        self.amount=amount
        self.__balance-=self.amount
        return self.__balance
b=BankAccount(900000000)
print(b.deposit(200000000))
print(b.withdraw(200000000))

class Person:
    def age(self,Age):
        self.__Age=Age
        if self.__Age>0:
            return self.__Age
        else:return "Invalid age"
p=Person()
print(p.age(23))



