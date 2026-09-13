i=1
while i<=10:
    print(i)
    i=i+1

# same task by for loop
for i in range(1,11):
    print(i)

for i in range(0,100,4):#this create difference of 4
    print(i)

# for loop for tuple
t=(2,4,5,"nigam")
for i in t:
    print (i)#this is also used in list ,strings and sets ,etc.
else:
    print("done") # this works when else statement is exhausted


l=["harry", 'david','Sachin','Rahul', 'ramesh']
for name in l:
    if(name.lower().startswith('s')):
        print("hello",name)
i=1
n= int(input("enter a number"))
while i<=10:
      print(f"{n} x{i}={n*i}")
      i +=1


n=int(input("Enter a number:"))# factorial example 5!= 5*4*3*2*1
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)

n=int(input("Enter a number:"))
for i in range (1,n+1):
   if n%(i+1)==0:
     print((n-1)*"* ",end="")
   else:print("* "*n,end="")
   print("")

n=int(input("Enter a number:"))
for i in range (1,n+1):
    print("*"*i)

n=int(input("Enter a number:"))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print('*', end="")
    print("")

i=10
n=int(input('Enter a number'))
while i>=1:
    print(f'{n}x{i}={n*i}')
    i-=1


