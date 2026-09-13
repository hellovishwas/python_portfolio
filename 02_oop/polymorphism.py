# Polymorphism means: same method name, different behavior
# Q-1
class Bird:
    def sound(self):
        print("ku-ku")
class Sparrow:
    def sound(self):
        print("chi-chi")
class Parrot:
    def sound(self):
        print("ram-ram")

b=Bird()
s=Sparrow()
p=Parrot()
s.sound()
b.sound()
p.sound()


# Q-2
class Circle:
    def area(self,radius):
        return 3.14*radius*radius
class Square:
    def area(self,side):
        return side*side
C=Circle()
S=Square()
print(C.area(5))
print(S.area(5))


class Employee:
    def work(self):
        return "general work"
class Manager:
    def work(self):
        return "manage team"
class Developer:
    def work(self):
        return "write code"
E=Employee()
M=Manager()
D=Developer()
print(E.work())
print(M.work())
print(D.work())


class Car:
    def drive():
        return "Drive Car"
class Bus:
    def drive():
        return "Drive Bus"
class Train:
    def drive():
        return "Drive Train"

t=Train.drive()
print(t)
c=Car.drive()
print(c)
b=Bus.drive()
print(b)



