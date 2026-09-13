# Map
l = [1, 2, 3, 4, 5]
square = lambda x: x * x
print(square(6))
sqlist = map(square, l)
print(list(sqlist))
