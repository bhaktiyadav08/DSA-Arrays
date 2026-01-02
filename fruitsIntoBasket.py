fruits=[3,3,3,1,2,1,1,2,3,3,4]
def fruitsIntoBasket(fruits):
    n=len(fruits)
    left, right = 0 , 0
    d={}
    max_len=0
    while right<n:     
         d[fruits[right]]=d.get(fruits[right],0)+1
         right+=1
         while len(d)>2:
            d[fruits[left]]-=1
            if d[fruits[left]]==0:
                del d[fruits[left]]
            left+=1
         max_len=max(max_len,right-left)
    return max_len
print(fruitsIntoBasket(fruits))

       
        
        
        
            
            


