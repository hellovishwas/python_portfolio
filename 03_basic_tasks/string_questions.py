'''
# QUES1 -Write a program that:
# Takes a string from the user
# Prints:
# Length of the string
# String in uppercase
# String in reverse
u=input("Enter a character:")
print(len(u))
print(u.upper())
print(u[::-1])
'''

# QUES2 - Create a list of 5 numbers.

# Perform the following operations:
# Add a number to the list
# Remove one number
# Sort the list
# Print the largest number
l=[1,3,5,8,5]
l.remove(1);print(l)
l.sort();print(l)
print(max(l))


# QUES3- Create a tuple of 5 elements.

# Write a program to:
# Print the tuple
# Count how many times a particular element appears.
t=(1,2,3,2,3)
print(t)
print(t.count(2))


# QUES4-Create a dictionary storing student name and marks.
# Add a new student
# Update marks of one student
# Print all student names.
d={"vishwas":90,"vedik":97,"jatin":88,"naman":70}
d["vedik"]=98
d["vikas"]=66;print(d)
print(d.keys())

# QUES5-Set Operations
# Create two sets:
# Find:

# Union
# Intersection
s0={1,4,5,5,6,3}
S1={'k',8,9,3,6}
u=print(s0.union(S1))
print(s0.intersection(S1))

# QUES6-Reverse a List Without Using reverse()
# Write a program to reverse a list manually

l=[1,3,5,8,5]
print(l[::-1])

# QUES7 - 
# Create a tuple of numbers and print the maximum value.
t=(1,2,3,2,3)
print(max(t))


# QUES8 -Write a program that finds unique elements from a list using set
l=[1,3,5,8,5]
f=set(l)
for i in f:
    print(i)
    
    
# QUES9- Write a Python program to store 10 numbers in a list and calculate their sum and average.
l=[1,3,5,8,5,9,0,3,0,6]
print(f"Sum:{sum(l)}",f"Average:{sum(l)/len(l)}")




# QUES10-. Write a Python function that
# accepts two numbers and returns multiple values:
#  sum
#  difference
#  product
#  division
def calculate(a,b):
    return a+b,a-b,a*b,a/b
print(calculate(110,23))
    