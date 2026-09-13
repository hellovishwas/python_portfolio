a=int(input("enter a number:"))
if a==1 or a==0:
    print("given number is neither composite nor prime") 
else:
    for i in range (2,a):
        if a%i==0:
            print("given number is composite")  
            break
    else: 
        print("given number is prime")    
        
        