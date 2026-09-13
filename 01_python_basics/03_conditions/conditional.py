age=int(input('enter your age:'))
#this is first if statement
if(age%2==0):
    print("age is even")#it is independent
# this is second if statement
if (age>=18):
    print("you are eligible")# this space is known as indentation
    print("for voting\nfor driving vechiles")
elif(age<0): print('you are entering invalid age')
else:print('you are not eligible')

# Odd and Even
a=int(input("enter a number"))
if a%2==0:
    print("a is even")
else:
    print("a is odd")

n = []
for i in range(100, 1001):
    if i % 11 == 0 and i % 2 != 0 and str(i) != str(i)[::-1]:
        n.append(i)
print(n)

# type of no
l = [1, 2, 3, 4, -1, -2, -3, -4, 0, 0, 0]
positive = 0
negative = 0
Zero = 0
for i in l:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        Zero += 1
print(positive)
print(negative)
print(Zero)
