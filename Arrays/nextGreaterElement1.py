nums1 = [4,1,2]
nums2 = [1,3,4,2]
def nextGreaterElement(nums1,nums2):
    res=[]
    stack=[]
    d={}
    for a in nums2:
        while stack and a>stack[-1]:
            d[stack[-1]]=a
            stack.pop()
        stack.append(a)
            
    for i in range(len(stack)):
        d[stack[i]]=-1
    for b in nums1:
       res.append(d[b])
    return res
print(nextGreaterElement(nums1,nums2))
    

