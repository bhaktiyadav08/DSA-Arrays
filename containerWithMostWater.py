height=[1,8,6,2,5,4,8,3,7]
def container(height):
    n=len(height)
    lb, rb = 0, n-1
    max_water=0
    while lb<rb:
        w=rb-lb
        ht=min(height[lb],height[rb])
        curr_water=w*ht
        max_water=max(curr_water,max_water)
        if height[lb]<=height[rb]:
            lb+=1
        else:
            rb-=1
    return max_water
print(container(height))      

