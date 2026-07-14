class Solution(object):
    def arrayRankTransform(self, arr):
        u_list=list(set(arr))
        u_list.sort()
        d={}
        rank=1
        for a in u_list:
            d[a]=rank
            rank+=1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr

