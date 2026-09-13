# function definition
def avg(): #it is user define function
    b=int(input('Enter first number:'))
    a=int(input('Enter second number:'))
    c=int(input('Enter third number:'))
    average=(a+b+c)/3
    print(average)
    print('done it')
    return"ok"
a=avg()
print(a)  #function call
avg()
avg()
avg()

def GoodDay(name):
    print("GoodDay,"+name)
GoodDay("vishwas")

name=input("enter your name:")
def GoodDay(name,ending="thank you"):
    print("GoodDay,"+name)
    print(ending)
GoodDay(name,"come again") #here it gives ending = come again
GoodDay(name) #if nothing is given here for ending then it gives thank you

a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

print(max(a,b,c))
t=float(input("Enter temperature in celsius:"))
def f(t):
    c=t*9/5+32
    return c
print(f"{round(f(t),2)}°fahrenhite")    # round function gives output only upto the no. you given
# to prevent new line in python use end=""
print("a")
print("b",end="")
print("c",end="")



n=int(input("Enter value in inches:"))
def c(n):
    return (2.54)*n
print(f"{c(n)}cms")

