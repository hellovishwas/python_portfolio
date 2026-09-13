h=int(input("Enter a number:"))
s=str(h)
l=len(s)
a=0
for r in range(1,l+1):
    o=int(s[-r])
    n=o**(l)
    a=n+a
if a==h:
    print(f"{h}  is armstrong number")
else:print(f"{h}  is not an armstrong number")

    
    
    