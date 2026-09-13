n=['vishwas',56,45,'uma',12,89,"jatin","hitesh",True]#list is a mutable collection of data
print(n)



n.append(8) 
print(n)    

n.insert(0,8)  
print(n)       


n.pop(-4)
print(n)

n.remove(45)  
print(n)

g=[45,56,99,'virat']
#Concatination
print(g+n)


#Extend 
g.extend('vishal')
print(g)





n={'Name':'vishwas', 'Age':20 , 'City':'Indore',"job":"A.I.engineer"} # creating a dictionary with keys and values
print(n)


# printing items of the dictionary
m=(n.items())
print(str(m))

# printing keys of the dictionary
p=n.keys()
print(str(p))

# printing values 
l=n.values()
print(str(l))

# adding values in list
n['Interest']= 'movies'
print(n)

# Updating values
n['Name'] = 'Uma'
print(n)

# Updating dictionary
n.update({'country':'India'})
print(n)

# Deleting items from dictionary
del n['City']
print(n)

#using pop method to delete items from dictionary
n.pop("Name")
print(n)



# dic={}
# print(type(dic))# it shows dictionary because it is empty
# tup=()
# print(type(tup))# it shows tuple because it is empty
# e=set()
# print(type(e))# it shows set because it is empty don't use {} for empty set because it shows dictionary 
s={1,2,3,4,4,4,2,5,5,5,'vishwas'}
print(type(s))# it shows set because it is not empty and repetion is not allowed in set
print(s)
s.add(6)# it is used to add element in set
print(s)
v={1,2,4,2,5,3}
# print(v.difference(s))
# print(s.difference(v))# it shows the difference between two sets
# print(len(s))
# s.remove('vishwas')# it is used to remove element from set if element is not present then it shows error
# print(s)
# s.pop()# it removes random element from set

# print(s)
print(s.union(v))# it is used to combine two sets
print(s.intersection(v))# it shows the common elements in both sets     
j=s-v# it shows the elements which are in s but not in v
print(j)
print({'vishwas',6}.issubset(s))# it checks whether the given set is subset of another set or not if yes then true else false



# tuple is the collection of different elements which , homogeneous or heterogeneous , ordered and immutable


n=(1,2,3,4,5,6,"vishwas","uma")  # creating a tuple with different data types
print(n)

# indexing
print(n[2])# accessing the 2nd element of the tuple

# reverse indexing
print(n[-1])

# accessing a bunch of items (slicing)
print(n[2:8]) # prints index of 2 to 7

#concotination 
g=(56,89,45,99)
print(n+g)

# repetition
print(g*5)

# membership operator
if 45 in g :
    print('exists')
else:
    print("not exists")


# length 
print(len(g))


# count method
print(n.count('uma'))
print(n.index('vishwas'))

# converting tuple to list
n=list(n)
print(type(n))
print(n)



