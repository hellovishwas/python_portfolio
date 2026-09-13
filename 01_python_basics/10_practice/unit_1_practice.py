#1.SYNTAX 
# set of rules which define how to write a program.
#grammar of any language.
#syntax is how to write a code in any particular language which can be understood by the interpreter to produce the desired output.

#2.INDENTATION
#it is the space given in a code syntax.

#example
'''if a==0:
     print("vishwas")'''
#the space before print is indentation.

#3.COMMENT
#lines that are not executed(ignored) by the interpreter.
#symbol of comment in python are #,''',,,''' and """...""".

#example:- here all the notes written with # are comments.

#4.VARIABLES
#memory vessels.
#name given to memory location where we store value or data.
#variables can be alphabetic, alphanumeric and can contain _.

#example :- u=25 ; here u is a variable.

#5.BUILT IN DATATYPES
#a. Numeric DataType[integer,float,complex]
#int : age=25
#float : height=6.2
#complex : 3+4j

#b. Text DataType
# string : "vishwas"

#c. Boolean DataType
#True/False

#d. Sequence DataType
# list,tuple

#e. Set DataType
# set {}

#f. Mapping DataType
# mapped in key-value pairs
#dictionary

#g. Binary DataType
#handles data which is in bits, ie, 0 and 1

#6.OPERATORS
#a.Arithmetic Operators : +,-,%,//,/,*
#float division(/) :- performs standard mathematical division and returns a floating point number.
#eg. 7/4=1.75
#floor division :- performs division and round down the result to the nearest whole number(towards negative infinity)
#eg. 7//4=1.75 is round off to 1
#modulus :- returns the remainder of the division.
#eg. 7%4=3


#b. Relational (Comparision) Operators : AND, OR, NOT
# AND : TRUE if both conditions True; FALSE if either condition is false.
#OR : TRUE if either condition is True.

#c. Bitwise Operator
# used to handle binary operations.

#d. Membership Operators[in, not in]
#used to know whether an element is a member of the given list,tuple,set,dictionary,string.
#checks a collection.

#example1
list3=["v","u","h","l","g"]
print("r" in list3)
print("r" not in list3)

#example2
list1=["t","r","o","p","h",'i','e']
list2=["r"]
print(list2 in list1)
print(list2 not in list1)#here only a strin "r" is present not whole  list2


#e. Identity Operator[is, is not]
#used to check whether the object is a member of a particular element.
#checks only 1 element.

#example1
str1="vedik"
str2="jayas"
print(str1 is str2)
print(str is not str2)

#example2
str1="vishwas"
str2="vishwas"
print(str1 is str2)
print(str is not str2)


a='vishwas'
b="vishwas"
print(a is b )#if string is small than python use same memory location
print(id(a))
print(id(b))


list1 = ['vishwas','virat','rohit']
list= ['vishwas','virat','rohit']
print(list is list1)# it defines whether the memory location is same or not
print(id(list))
print(id(list1))

#f. Assignment Operator
#it is used to assign a value to a variable.

#example :- x=22 here = is the assignment operator.


# # list
# mylist=[101,"vishwas",100.2,]#list is the collection of homogenous and heterogenous data
# print(mylist)

# mylist.append(300)
# print(mylist)#List is mutable and allowed duplicate element
# mylist.remove("vishwas")
# print(mylist)

# mylist[1]="Rajesh"
# print(mylist)


# # Tuple
# #Tuple is the collection of homogenous and heterogenous data and represented by()
# mytuple=()
# mylist=[]
# print(type(mytuple))#Tuple is an immutable data type
# print(type(mylist))


# m=10
# print(type(m))#output (int)
# m=(10)
# print(type(m))#output (int)
# m=(10,)
# print(type(m))#output (tuple) this is the way to make tuple with single element



# set{}
# m1={}# this is dictionary
# m1=set({})#this is empty set
# m2=frozenset({1,2,3,"jatin",3}) #order is not necessary to be same in set and frozenset and not allowed duplicacy
# print(type(m2))#frozen set is immutable data type

#dictionary
# mydict={101:"shivansh",102:"vishwas",103:"pari",102:"paridhi"}
# print(mydict)


# ##function
# def addition():
#     a=20
#     b=30
#     c=(a+b)
#     print(c)
# # Main
# addition()


# def addition(a,b):
#     c=(a+b)
#     print(c)
# # Main here call function
# addition(20,30)

# def sqrt():
#     a=25
#     print(a**(1/2))
# sqrt()



# ##File Handling in Python

# 1st step open the file
# perform file handling operation
# close the file
# write mode=w   write mode always overwrite the existing data
# append mode=a  append mode always add the new data at the end of the existing data
# read mode=r    read mode always read the existing data
# create=x       create mode always create the new file if the file is not existing if file is existing it will give error
''' 
f=open("c://iamvishwas/student.txt","a")
f.write("\nvirat\nrohit")
f.close()
print("File created-------------")
'''
f=open("c://mysage/students.txt","a")

while (True):
        id=input("Roll NO.")
        name=input("Name:")
        course=input("course:")
        info=name+","+id+","+course
        f.write(info)
        choice=input(" Enter your choice y/n")
        if (choice.lower()=="n"):
            break
print("file created or updated...............")



#7.BUILT-IN FUNCTIONS
# a. i/o Function
#for input : input()
#for output : print()

#example
a=input("Enter your name: ")
print(a)

#b. Type Conversion Function
#used to convert the datatype.
#int(),str(),float(),tuple(),list(),dictionary().

#example
a="vishwas"
print(list(a))
print(tuple(a))

b=13.5
print(int(b))

# List to tuple

g=[29,23,46,'vishwas','vedik',20]

n= tuple(g)
print(type(n))

# dictionary to tuple

g={'Name': 'vishwas','About': 'JEE Aspirant','Age': 20}
s=tuple(g.items())
print(type(s))



#c. Mathematic Functions
#used to perform mathematical caculations.
#min(),max(),sum(),pow(),round().
print(pow(2, 3))
print(round(2.567, 2))
print(max(5, 9, 2))
print(min(5, 9, 2))
print(sum([1, 2, 3, 4]))

#d. Sequence Utilities Function
#functions we use after creating collections(list,tuple,dictionary).
#len(),reverse(),sort(),append(),insert().
numbers = [10, 20, 30, 40]
print(len(numbers))
numbers.append(50)
print(numbers)
numbers.insert(1, 15)   # index 1 par 15 add
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)#ascending order
#e. Object Classification Function[type()]
#used to know the type of element /obejct.

#example
l=450
m=45.57
n="vedik"
o=3+5j
p=[1,2,3]
q=(2,4,6)
r={"name":"vishwas","age":18}
print(type(l))
print(type(m))
print(type(n))
print(type(o))
print(type(p))
print(type(q))
print(type(r))

#f. Memory Address Funtion[id()]
#used to know the momory address of an element /object.

#example
b="vishwas" 
print(id(b))

#g. Function Programming Helpers
#the built-in functions which help us to define a function.

#ITERABLES :- object(list,tuple,dictionary,set) that has ability to return item/element one at a time.
#used in for loops

#i) Map() - apply funtion on iterables.
numbers = [1, 2, 3, 4]

result = map(lambda x: x**2, numbers)
print(list(result))
#ii) Zip() - for combining iterables.
names = ["Ram", "Shyam", "Mohan"]
marks = [80, 90, 70]

result = zip(names, marks)
print(list(result))
#iii) Filter() - keeps items that match the condition.
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

#h. Concatenation[+]
#used to add strings.
#two collection(list,tuple,dictionary,set) can also be added.

#example
a="virat"
b="kohli"
c=a+b
print(c)

#i. Replication[*]
#used to multiple an element or string.

#example
a="vishwas,  "

print(a*3)

#8.ESSENTIAL PYTHON LIBRARIES
#1. Numpy
#used for numerical computing in python.
#it has data structure, algorithms and library required for most application involving numerical data.

#Array
#a special variable which can hold more than one value at a time.
#implemented through internal libraries(np.array).
#a collection of items stored at continous memory location.

#2. Pandas
#helps in working with structured and tabular data fast and easy.
#has high level data structures and functions.
#have flexible data manipulation capabilities of spreadsheet and relational databases(such as SQL).

#3. Matplotlib
#used for producing plots and other 2-D data visualizations.
#can create plots suitable for publication.

#4. Statsmodel
#used for classical statistics and econometics.

#5. Scipy
#used for scientific or mathematics expressions.

#6. Scikitlearn
#contails all that we learnt about ML in 1st sem.





