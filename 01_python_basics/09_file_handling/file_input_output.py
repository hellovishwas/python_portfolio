f=open("list.py") #list file is open in terminal
data=f.read()
print(data)
f.close()
st="vishwas is amazing"
f=open("myfile.txt",'w')#str is add in myfile.txt
f.write(st)
f.close()
f=open("myfile.txt")
lines=f.readlines()
print(lines,type(lines))
f.close()
f=open("myfile.txt")# it always give str as type of lines
line1= f.readline()
print(line1,type(line1))
line2= int(f.readline())#until you write type in input
print(line2,type(line2))
line3= f.readline()
print(line3,type(line3))
line4= f.readline()
print(line4=="")
# this code can also be written by using while loop
f=open("myfile.txt")
line =f.readline()
while line!="":
    print(line,type(line))
    line=f.readline()
f.close()
#one more way to write this code with using "with" statementN
with open("myfile.txt") as f:
    print(f.read())
t=open("poem.txt")
content=t.read()
if ("twinkle" in content):
    print("the word twinkle is present in the content")
else:print("the word twinkle is not present in the content")
t.close()
t=open('dic.py')
content=t.read()
print(content)
t.close()


import random
def game():
    print("you are playing a game...")
    score=random.randint(1,62)
    with open ('hiscore.txt') as f:
        hiscore=f.read()
        if hiscore!="" :
            hiscore=int(hiscore)
        else: hiscore=0
    print(f"Your score:{score}")
    if (score>hiscore ):
        # write this hiscore to the file
        with open ("hiscore.txt", "w") as f:
            f.write(str(score))                 #if score is greater than previous score than it will be updated  on hiscore.txt
    return score
game()



for i in range (1,21):
    filename=f'table{i}.txt'
    with open(filename,"w") as f:
        f.write(f"Table of {i}\n")
        for j in range (1,11):
            table= f"{i} x {j} = {i*j}\n"
            f.write(table)


with open ('donkeypoem.txt','r') as f:
    content=f.read()
contentnew=content.replace('donkey',"#####")
with open ('donkeypoem.txt','w') as f:
    content=f.write(contentnew)

word="python"
with open ('log.txt') as f:
    lines=f.readlines()
found= False
for line_no, line in enumerate (lines, start=1):
    if word in line:
        print(f"word found in line {line_no}: {line.strip()}")
        found= True

with open ("log.txt") as f:
    content=f.read()
with open ("logarithm.txt","w") as f:
    f.write(content)


with open ("log.txt") as f:
    content=f.read()
with open ("log.txt") as k:
    data=k.read()
if data==content:
    print("Both files are identical")
else:print("Both files are unidentical")

with open ("poem.txt","w") as f:
    f.write(" ")#this can wipe out file


with open ("log_copy.txt","r") as f:
    content=f.read()
with open ("python.txt","w")as f:
    f.write (content)#this can rename your file
