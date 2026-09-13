
class Employee:
    name= "vedik"
    language="py"
    salary=1200000
    def __init__(self, name,salary,language):#this is dunder method .You don't need to call it.
        self.name=name                       #THIS IS INSTANCE ATTRIBUTE
        self.salary=salary
        self.language=language
        print("I am creating an object")

    @staticmethod #greet is the static method it means not needs of object(self)
    def greet():
        print("Good Morning")
    def getinfo(self):
        print(f"The name is {self.name}.The language is {self.language}.The salary is {self.salary}.")
FirstEmployee=Employee("vaibhav",130000,"javascript")
FirstEmployee.greet()
FirstEmployee.getinfo()


class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode
    def getinfo(self):
        print(f"The Company name is {self.company}. The Employee name is {self.name}. The Salary is {self.salary}. The Pincode is {self.pincode}")
Programmer1=Programmer("Vishwas",1200000000,452003)
Programmer2=Programmer("Ved",120000,45003)
Programmer3=Programmer("Harsh",12000000,45203)
Programmer1.getinfo()
Programmer2.getinfo()
Programmer3.getinfo()


# x=int(input("Enter a number:"))
# class calculator:
#     @staticmethod
#     def hello():
#         print("Hey there")

#     square=x**2
#     cube=x**3
#     sqrt=x**(1/2)
#     print((fSquare={square}
#                 Cube={cube}
#                 Sqrt={sqrt}))

# class Demo:
#     a=4#this is class attribute
# o=Demo()
# print(o.a)#output;4
# o.a=0#instance attribute
# print(o.a)#output;0
# print(Demo.a)#output;4   this means class attribute is not changed



from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no.:{self.trainNo} from '{fro}' to '{to}'.")
    def getstatus(self):
        print(f'Train no:{self.trainNo} is running on time.')
    def getfare(self,fro,to):
        print(f"Ticket Price in train no. {self.trainNo} from '{fro}' to '{to}' is {randint(100,400)}.")
t=Train(13233)'
t.book('Indore','Bhopal')
t.getstatus()
t.getfare('Indore','Bhopal')



class change:
    def __init__(slf,name,age):
        slf.name=name
        slf.age=age
    def getinfo(slf):
        print(f"The name of user is {slf.name} and age is {slf.age}.")
c=change("vedik",16)
c.getinfo()

