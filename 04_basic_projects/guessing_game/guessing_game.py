from random import randint
print("\"Welcome to the number guessing game\"\nYou have to choose integer b/w \"0 to 100\"")
computer=randint(1,100)
user=0
i=0
while user!=computer:
    try:
        user=int(input("Enter a number:"))
        if user== computer:print("Congrates!You won the game")
        elif (user-computer)>=20 :print("You are too far.Try a smaller number")
        elif 0<(user-computer)<=20 :print("You are too close.Try a slightly smaller number")
        elif (computer-user)>=20:print("You are too far.Try a greater number")
        elif 0<(computer-user)<=20:print("You are too close.Try a slightly greater number")
        else:print("Invalid input")
        i=i+1
    except ValueError:print("Invalid Choice.")
print("Correct number is:",computer) 
print("Number of tries:",i)
    


    