
class Employee:
    language="Python"
    salary=120000
    def __init__(self):#dunder method automatically called
        print('I am creating an object')
    def getinfo(self):
        print(f"The name of employee is {self.name}.The language is {self.language}.The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

obj=Employee()
vishwas=Employee()
vishwas.name="Vishwas Sharma"
vishwas.getinfo()
print(vishwas.salary)
Employee.getinfo(vishwas)
Employee.greet()

class programmer:
    company="microsoft"
    def __init__(self,name,language,designation,salary):
        self.name=name
        self.salary=salary
        self.language=language
        self.designation=designation
    def getinfo(self):
        print(f"The name of company is {self.company},The name of employee is {self.name}.The language is {self.language}.The salary is {self.salary}.The designation of employee is {self.designation}.")


p=programmer("Harry","Js","CEO",122000)
p.getinfo()



class Calculator:
    def __init__(self,a):
        self.a=a
    def sqr(self):
        print(f"The square is:{self.a*self.a}")
    def sqrt(self):
        print(f"The square root is:{self.a**(1/2)}")
    def cube(self):
        print(f"The cube is:{self.a**(3)}")
    @staticmethod
    def hello():
        print("Hello there")
h=Calculator(4)
h.cube()
h.hello()
class Demo:
    a=4

o=Demo()
print(o.a)
o.a=0
print(Demo.a)#no change in class attribute
print(o.a)
import random
class Train:
    def book(self,trainno,fro,to):
        print(f"Ticket is booked in traiNo:{trainno} from {fro} to {to}")
    def getstatus(self,trainno):
        print(f"The trainNo is {trainno} is runninng on time")
    def getFare(self,trainno,fro,to):
        print(f"Ticket fare in trainNo :{trainno} from {fro} to {to} is:{random.randint(29,500)}")
t=Train()
t.getFare(123,"Indore","Bhopal")
t.book(123,"Indore","Bhopal")
# t.getstatus(123)

class Employee:
    def __init__(self):
        print("constructor of Employee")
    company="Tata"
    name="vishwas"
    salary=6700000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
class coder:
    def environment(self,env):
        print(f"The environment is {env} used by coder")
class Programmer(Employee,coder):
    def __init__(self):
        super().__init__()
        print("constructor of manager")
    company="ITC"
    def showlanguage(self,language):
        print(f" he is good with {language} language")
a=Employee()
b=Programmer()
c=coder()
c.environment("VS code")

a.show()
b.showlanguage("python")
print(a.company,b.company)

class Employee:
    language="py"#This is a class attribute
    salary=120000
FirstEmployee=Employee()
FirstEmployee.name="Vedik"#This is an instance attribute
print(FirstEmployee.name,FirstEmployee.language,FirstEmployee.salary)
SecondEmployee=Employee()
SecondEmployee.name="Rakesh"
print(SecondEmployee.name,SecondEmployee.language,SecondEmployee.salary)
FirstEmployee.language="c++"
print(FirstEmployee.name,FirstEmployee.language,FirstEmployee.salary)#this shows that instance attribute take preferefnce over class attribute
def myfunc():
    print("Hello vishwas!")
myfunc()
print(__name__)#output =__main__


class Employee:
    name= "vedik"
    language="py"
    salary=1200000
    @staticmethod #greet is the static method it means not needs of object(self)
    def greet():
        print("Good Morning")
    def getinfo(self):
        print(f"The name is {self.name}.The language is {self.language}.The salary is {self.salary}.")
FirstEmployee=Employee()
FirstEmployee.getinfo()
FirstEmployee.greet()

class Students:
    def nme(self, name):
        return name

    def mark(self, marks):
        return marks


s = Students()
print(s.mark(67))
print(s.nme("vishwas"))


class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


c = Calculator()
print(c.sum(1, 2))


class Bankaccount:
    def __init__(self):
        self.bank_balance = 1200000

    def deposit(self, amount):
        self.bank_balance += amount
        print(f"{self.bank_balance + amount} is your current bank balance.")

    def withdraw(self, amount):
        self.bank_balance -= amount
        print(f"{self.bank_balance - amount} is your current bank balance.")


b = Bankaccount()
b.deposit(500000)
b.withdraw(500000)


class Animal:
    def leg(self):
        print("Animal has 4 legs")


class dog(Animal):
    def bark(self):
        print("bow bow")


d = dog()
d.bark()


class Person:
    def brain(self):
        print("A person have a brain")


class Student(Person):
    def nme(self, name):
        self.name = name
        return self.name

    def mark(self, marks):
        self.marks = marks
        return self.marks


c = Student()
c.brain()
print(c.nme("vishwas"))
print(c.nme(99))


class Car:
    def start(self):
        print("Car started")


c = Car()
c.start()


class Mobile:
    company = "Samsung"

    def brand(self):
        print(f"Brand name of mobile is {self.company}")


m = Mobile()
m.brand()


class Book:
    def title(self, name):
        self.name = name
        return self.name


b = Book()
print(b.title("Harry Potter"))


class student:
    def std(self, name, marks):
        self.name = name
        self.marks = marks


s = student()
s.std("vishwas", 99)
print("Name:", s.name)
print("Marks:", s.marks)


class Circle:
    def info(self, radius):
        self.radius = radius


c = Circle()
c.info(4)
print("Radius of circle:", c.radius)


class Laptop:
    def info(self, brand, price):
        self.brand = brand
        self.price = price


l = Laptop()
l.info("Lenovo", 36000)
print(
    "The brand of the laptop is {} and price of the laptop is {}.".format(
        l.brand, l.price
    )
)


class Rectangle:
    def area(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print(f"The area of rectangle is {self.length * self.breadth}")


r = Rectangle()
r.area(2, 8)


class Employee:
    def details(self, name, salary):
        self.name = name
        self.salary = salary


E = Employee()
E.details("Vishwas", 8200000)
print(
    f"The name or the employee is {E.name} and monthly package of Employee is {E.salary}."
)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Vishwas", 20)
print(f"The name of the person is {p.name} and age of the person is {p.age}.")


class Dog:
    def __init__(self, breed, color):
        self.color = color
        self.breed = breed


d = Dog("German Shepherd", "Black")
print(f"The breed of the Dog is {d.breed} and color of its is {d.color}.")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


f = Product("Rolls Royce", 120000000)
print(
    f"The name of the precious product is {f.name} and price of this royal beauty is {f.price}."
)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s = Student("Vishwas", 99)
if s.marks >= 40:
    print(f"The status of the {s.name} with marks {s.marks} : PASS")
else:
    print(f"The status of the {s.name} with marks {s.marks} : FAIL")


class Animal:
    def info(self):
        print("Animal has long tail")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


d = Dog()
d.info()
d.bark()


class Vehicle:
    def info(self):
        return "The vehicles are run by using power of engine."


class Bike(Vehicle):
    def wheels(self):
        return "Bike has two wheels."


b = Bike()
print(b.wheels())
print(b.info())


class Shape:
    def property(self):
        print("It is the boundary line.")


class square(Shape):
    def area(self, a):
        self.a = a
        return self.a * self.a


s = square()
s.property()
k = s.area(2)

print(f"The area of the square having side {s.a} is {k}.")


class Bankaccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"The bank balance in your account is {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        print(f"The bank balance in your account is {self.balance}")


b = Bankaccount(16000000)
b.deposit(4000000)
b.withdraw(600000)


class Library:
    def __init__(self, books):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def show(self):
        print(self.books)


l = Library("kk")
l.add("Alchemist")
l.add("Harry Potter")
l.show()


class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, loss):
        self.loss = loss
        self.health -= self.loss
        print(f"Remaining health of {self.name} is {self.health}.")


ch = GameCharacter("Ashwin", 100)
ch.attack(10)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, *item):
        for i in item:
            self.items.append(i)
        print(f"The list of items after adding a new element {self.items}")

    def rem(self, *item):
        for i in item:
            self.items.remove(i)
        print(f"The list of items after removing a new element {self.items} ")


s = ShoppingCart()
s.add("Lamborgini", "Ferrari", "Mustang", "Ninja H2R")
s.rem("Mustang")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def introduction(self):
        print(f"Hello,I am {self.name} and I tech {self.subject}")


t = Teacher("Vishwas", "Python")
t.introduction()


class calculator:
    def plus(a, b):
        print(a + b)

    def minus(a, b):
        print(a - b)

    def mul(a, b):
        print(a * b)

    def div(a, b):
        if b == 0:
            print("NOT DEFINED")
        else:
            print(a / b)
