# raising error
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if b == 0:  # It gives error
    raise ZeroDivisionError("Your programme is not meant to divide numbers by zero")
else:
    print(f"the division a/b is {a / b}")


# try-finally #finally  humesha chalega
def main():
    try:
        a = int(input("hey,Enter a number:"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("hey I am inside of finally")


main()


# try-else#else tab hi chalega jab try statement sahi hogi
try:
    a = int(input("hey,Enter a number:"))
    print(a)
except Exception as e:
    print(e)
else:
    print("hey I am inside of else")
