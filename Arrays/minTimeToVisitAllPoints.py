points = [[1,1],[3,4],[-1,0]]
def minTimeToVisitAllPoints(points):
    time=0
    for i in range (1,len(points)):
        dx=points[i-1][1]-points[i][0]
        dy=points[i-1][1]-points[i][0]
        time+=max(dx,dy)
    return time
print(minTimeToVisitAllPoints(points))
        
