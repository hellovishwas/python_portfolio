l=[1,2,4,5,3]
print(sum(l))
# or
def summation(*args):
    n=0
    for i in args:
        n=n+i
    return(n)
print(summation(*l))