n=int(input("Enter no of terms : "))
l=[0,1]
a=0
for i in range (0,n-2):
    a=l[i]+l[i+1]
    l.append(a)
for i in l:
    print(i)

    