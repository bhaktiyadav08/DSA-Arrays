cost=[6,5,7,9,2,2]
def minCostCandy(cost):
    cost.sort(reverse=True)
    free=[]
    res=0
    i=0
    while i<len(cost):
        res+=cost[i]
        if i+1 < len(cost):
            res+=cost[i+1]
        if i+2 < len(cost):
            free.append(cost[i+2])
        i=i+3
    return res
print(minCostCandy(cost))



    
