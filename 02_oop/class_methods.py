class Employee:
    salary = 1200000
    increment = 12

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

e = Employee()
print(e.salaryAfterIncrement)   # works
e.salaryAfterIncrement = 1344000
print(e.increment)             # 12.0  (or updated value)
print(e.salaryAfterIncrement)   # still 1344000 as expected



class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c):
        return Complex(self.r+c.r,self.i+c.i)
c1=complex(1,2)
c2=complex(3,4)
print(c1+c2)


