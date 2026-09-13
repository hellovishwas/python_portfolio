binary=input("Enter a number:")
l=len(binary)
power=l-1
decimal=0
if all(ch in "01" for ch in binary):
    for num in binary:
        decimal=decimal+int(num)*(2)**power
        power-=1
    print(decimal)
else:print("Binary number contains only 0 or 1") 

    



