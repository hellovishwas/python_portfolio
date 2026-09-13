# class Google: #When a function is a part of class then it is method
#     def search(self):
#         print("This is search")
class Test1:
    def add(self):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=(a+b)
        print(c)
    def sub(self):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=(a-b)
        print(c)
    def mul(self):
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        c=(a*b)
        print(c)
    
t=Test1()#t is object having properties and method
t.add()
t.mul()


class Test2(Test1):# it is inheritance test2 has all properties of test1
    def sqrt():
        a=int(input("Enter first number"))
        print(a**(1/2))
    
