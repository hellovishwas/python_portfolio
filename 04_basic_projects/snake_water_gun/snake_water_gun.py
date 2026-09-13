import random
youstr=input("enter your choice: ")
computer=random.choice([1,2,3])
youdict={"snake":1, "water":2, "gun":3}
reversedict={1:"snake",2:"water",3:"gun"}
you=youdict[youstr]
computerstr=reversedict[computer]
print(f"you  choose {youstr}\ncomputer choose {computerstr}")
if (computer==you):
    print("Its a draw")

else:
    if(computer==1 and you==2):
        print("You Lose")
    elif(computer==1 and you==3):
        print("You Win")
    elif(computer==2 and you==1):
        print("You Win")
    elif(computer==2 and you==3):
        print("You Lose")
    elif(computer==3 and you==2):
        print("You Win")
    elif(computer==3 and you==1):
        print("You Lose")
    else:
         print("something went wrong")
        
    
    
