nums=[21,21]
def fourDivisors(nums):
    total=0
    for num in nums:
        res=[]
        n=int(num**0.5)
        for i in range(1,n+1):
            if num%i ==0:
                res.append(i)
                if i!=(num//i):
                    res.append(num//i)
        if len(res)==4:
                total+=sum(res)
    return total
print(fourDivisors(nums))


      

 