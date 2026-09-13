username="Vishwas Sharma"
password="secret"
while True:
    n=input("Enter your name:")
    m=input("Enter your password:")
    if username==n and password==m:
        print(f"Welcome!{username}")
        break
    else:print("You entered wrong info")


