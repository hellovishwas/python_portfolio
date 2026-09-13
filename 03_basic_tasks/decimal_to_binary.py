n=int(input("Enter a number"))
quotiont=n
binary=''
while quotiont>0:
    remainder=quotiont%2
    quotiont=quotiont//2
    binary=str(remainder)+binary
print(binary)
    
