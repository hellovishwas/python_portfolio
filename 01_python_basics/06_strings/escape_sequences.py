a='''vishwas is a good boy
 but not a bad boy'''
print(a)
# or we can also use \n for new line
a="vishwas is a good boy \n but not a bad boy"
print(a)
a="vishwas is a good boy \t but not a bad boy" #\t is used for tab space
print(a)
a="vishwas is a good boy \b but not a bad boy" #\b is used for backspace
print(a)
a= "Vishwas is a good \"boy\" " #\" is used to print " in str
print(a)
a=input("enter a character:")
print(a.count('o'))

name= input("enter your name")
print("good afternoon", name)
name=input("enter your name")
print(f"good afternoon {name}")# using f str and curly bracket
letter='''Dear <|Name|>,
        You are selected!
        <|Date|>'''
print(letter.replace("<|Name|>","vishwas").replace("<|Date|>","24 septmber 2025"))
a= "a b c  d"
print(a.find("  "))# if not exist then -1 is output
print(a.replace("  ", " "))
letter="dear vishwas,\n\t this python course is nice.\nThanks!"
print(letter)

name='vedik'
print(name[1:3])
name = "0123"  # str can also be written in '' and for multiline we can use """ """
print(name[0:3])# it is slicing
print(name[:4])#it is same as print(name[0:4])
print(name[1:])#it is same as print(name[1:4])
print(name[:])#it is same as print(name[0:4])
print(name[-1:-3])# it will not print anything because -1 is greater than -3
print(name[-3:-1])# it will print 12 because -3 is less than -1
print(t)
a="abcdefghijklmnopqrstuvwxyz"
print(a[1:3:5])
print(a[:])#if nothing is written before :(colon) then it assume 0 there and after :(colon) it assume last character of str
print(a[-4:-3])
a=input("enter a string:")
print(a[-11::-1])#it will print the str in reverse order
