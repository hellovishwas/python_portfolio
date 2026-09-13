h=int(input("Enter a number:"))
s=str(h)
l=len(s)
j=1
reverse=0
for r in range(1,l+1):
    o=int(s[-r])
    n=o*(10)**(l-j)
    j+=1
    reverse=reverse+n
    
print(reverse)




