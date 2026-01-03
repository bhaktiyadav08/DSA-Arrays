n=2
def paintNby3(n):
    if n==0:
        return 0
    two=6
    three=6
    n-=1
    while n>0:
     nextTwo=(two*3+three*2)
     three=(2*two+2*three)
     two=nextTwo
     n-=1
    return (two+three)%(10**9+7)
print(paintNby3(n))
    
