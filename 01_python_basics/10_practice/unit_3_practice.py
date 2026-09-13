##Write a program that:
##Takes a string from the user

s=input("Enter a character:")
print(len(s))#length of string
print(s.lower())#string un lowercase
print(s.upper())#string in uppercase
print(s[::-1])#reverse the string
##Create a list of 5 numbers.
l=[1,3,5,6,7]
print(sum(l))
l.pop(0)
print(l)
l.sort()
print(l)
print(max(l))
##
t=(8,2,5,9,1,8)
print(t)
print(t.count(8))
##
d={"Vishal":87,"Anuj":63,"Rohit":45}
d["Vishal"]=45
d["Jatin"]=89
print(d)
o=d.keys()
for i in o:
    print(i)
##
s={1,2,3,4,7}
v={0,9,8,7,5}
print(s.union(v))
print(s.intersection(v))
##
ls=["j",9,True,0]
s=[]
for h in ls:
    s.insert(0,h)
print(s)
# ##
b=(1,4,7,3,0,12)
print(max(b))
##
l=["n","m",90,90 ,"jatin","fish",'n']
print(set(l))
##
l=[1,2,3,4,5,6,7,8,9,0]
print(f"sum of list is :{sum(l)}")
print(f"average of list is {sum(l)/len(l)}")
##
n=float(input("Enter first number:"))
m=float(input("Enter second number:"))
print("Addition is",(m+n))
print("Subtraction is" ,(n-m))
print("Multiplication is",(m*n))
if m==0:
    print("Not defined")
else:
     print("Division is",(n/m))
    


