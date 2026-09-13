import random
print("Welcome\nYou have to choose ""rock"",""paper"" or ""scissors""")
l=["rock","paper","scissors"]
computer=random.choice(l)
choice=input("Enter your choice:")
if choice==computer:print("Congratulation!You won the game")
elif choice not in l:print("Invalid Choice")
else:print("Oops!You lose the game");print(f"Correct choice is {computer}")
