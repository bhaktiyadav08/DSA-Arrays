s="1000100"
def maxActiveSections(s):
    max_l=0
    i=0
    count=0
    for a in s:
         if a=='1':
            count+=1
    s='1'+s+'1'
    while i<len(s):
        
        if s[i]=='1':
            start=i
            while i<len(s) and s[i]=='1':
                i+=1
            end=i-1
            
            if end+1<len(s) and s[start-1]=='0' and s[end+1]=='0':
                left=start-1 
                while left>=0 and s[left]=='0':
                 left-=1
                left+=1
           
                right=end+1
                while right<len(s) and s[right]=='0':
                 right+=1
                right-=1
                removed = end - start + 1
                merged = right - left + 1
                gain = merged - removed 
                if gain > max_l:
                  max_l = gain
        else:
            i+=1
    
    res=count+max_l
    return res
    
print(maxActiveSections(s))