s='z*#'
def preprocessStr(s):
    result=''
    for s1 in s:
        if s1>='a' and s1<='z':
            result+=s1
        elif s1=='*':
            result=result[:-1]
        elif s1=='#':
            result*=2
        elif s1=='%':
            result=result[::-1]
        else:
            continue
    return result
print(preprocessStr(s))