n=input("Enter a character:")
reverse=n[::-1]
if n==reverse:
    print(f"{n} is palindrome")
else:print(f"{n} is not palindrome")