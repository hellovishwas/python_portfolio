from random import randint
choice=0
print("\"Welcome to the DICE SIMULATOR\"")
while choice!="stop":
    choice=input("Enter your choice:")
    if choice=="roll":n=print(randint(1,6))
    elif choice=="stop":print("Thanks for playing.I hope you enjoy it.")
    else:print("Invalid input")

