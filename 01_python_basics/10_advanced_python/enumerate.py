# Enumerate
l = [3, 233, 45, 34, 65]
index = 0
for i in l:
    print(f"The item number at index {index} is {i}")
    index += 1
# This can be simplified using enumerate function
for index, i in enumerate(l):
    print(f"The item number at index {index} is {i}")
