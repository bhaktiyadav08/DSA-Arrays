s='1000111'
def checkOnesSeg(s):
 i=1
 while i<(len(s)):
    if s[i]=='1':
     i+=1
     continue
    else:
     i+=1
     if i<(len(s)) and s[i]=='1':
      return False
 return True
print(checkOnesSeg(s))




