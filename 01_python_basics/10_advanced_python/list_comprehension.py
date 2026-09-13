# List comprehension
myList = [1, 2, 3, 4, 5, 6, 7, 8]
squaredList = []
for item in myList:
    squaredList.append(item**2)
print(squaredList)

squaredList = [i**2 for i in myList]
print(squaredList)


n = int(input("Enter a number:"))
l = list(range(n, 0, -1))
print(l)
