s = "ababcbacadefegdehijhklij"
def partitionLabels(s):
    res=[]
    beg=0
    d={}
    for k in range(len(s)):
       d[s[k]]=k
    while beg<len(s):
      max_len=1
      i=beg
      while i <beg+max_len:
        curr=d[s[i]]-beg+1
        max_len=max(curr,max_len)
        i+=1
      beg+=max_len
      res.append(max_len)
    return res
print(partitionLabels(s))


        
