l=[]
m=int(input("enter first number"))
n=int(input("enter second number"))
for i in range(m+1,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         l.append(i)
print(l)
print(sum(l))

