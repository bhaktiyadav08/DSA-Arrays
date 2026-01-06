fruits = [4,2,5]
basket = [3,5,4]
def fruitsIntoBasket2(fruits, basket):
    n=len(basket)
    used=[False]*n
    for fruit in fruits:
        placed=False
        for j in range(n):
            if not used[j] and basket[j]>=fruit:
                used[j]=True
                placed=True
                break
        if not placed:
            return 1
    return 0
print(fruitsIntoBasket2(fruits,basket))
            
    
    

2,4,5
3,4,5
