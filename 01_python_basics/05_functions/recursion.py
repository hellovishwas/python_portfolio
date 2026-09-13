'''Recursion means defining something in terms of itself.

In simple terms:

It’s when a process repeats by calling or referring back to itself.
Each repetition usually moves toward a stopping point (called a base case).'''
def factorial(n):
    if(n==1 or n==0): 
        return 1 
    return  n*factorial(n-1)

n=int(input("Enter a number:"))
print(f"The factorial of this number is, {factorial(n)}")
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

n=int(input("Enter a number:"))
print(f"sum of natural number is {sum(n)}")
n=int(input("Enter a number"))
def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)
print(pattern(n))

        