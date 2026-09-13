a=56
def fun():
    global a#it changes the value of a
    a=3
    print(a)
fun()
print(a)