s = "a#c"
t = "b"
def backspaceCompare(s,t):
    a1=[]
    a2=[]
    for s1 in s:
        if a1 and s1=='#':
            a1.pop()
        elif not a1 and s1=='#':
            pass
        else:
            a1.append(s1)
    for s2 in t:
        if a2 and s2=='#':
            a2.pop()
        elif not a2 and s2=='#':
            pass
        else:
            a2.append(s2)
    if a1==a2:
        return True
    else:
        return False
print(backspaceCompare(s,t))

