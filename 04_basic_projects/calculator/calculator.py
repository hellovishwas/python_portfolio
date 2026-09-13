print("\"Welcome To Our Calculator\"")
choice=0
while choice!="6":
    try:
        print("1.add(+)\n2.subtract(-)\n3.multiply(x)\n4.divide(/)\n5.power(^)\n6.Exit🔙")
        choice=input("Enter your choice:")
        if choice=="1":
          n=float(input("Enter first number:"))
          m=float(input("Enter second number:"))
          print("Addition is",n+m)
        elif choice=="2":
            n=float(input("Enter first number:"))
            m=float(input("Enter second number:"))
            print("Subtraction is",n-m)
        elif choice=="3":
            n=float(input("Enter first number:"))
            m=float(input("Enter second number:"))
            print("Multiplication is",n*m)
        elif choice=="4":
            n=float(input("Enter numerator:"))
            m=float(input("Enter denometer:"))
            if m==0:
                print("NOT DEFINED💭")
            else:
                print(f"Division is {n/m:.2f}")
        elif choice=="5":
            n=float(input("Enter base number:"))
            m=float(input("Enter power:"))
            if n==0 and m<0:
                print("NOT DEFINED💭")
            else:
                print(f"Output is {(n)**(m):.2f}")
        elif choice=="6":print("Thanks!I hope it is helpful for you😊.")
        else:print("Invalid Choice")
    except ValueError:print("Invalid Input🫨.")               
    except OverflowError:print("Very large input to solve🤯.")     



