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
