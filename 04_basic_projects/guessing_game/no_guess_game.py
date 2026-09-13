from random import randint
computer=randint(1,11)
n=int(input("Enter a number:"))
if n==computer:
    print("Congratulations!You win the game.")
else:print("Oops!You lose the game.");print(f"The number is {computer}")
       