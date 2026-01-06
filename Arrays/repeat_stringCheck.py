def repeat_check(arr):
    freq={}
    repeated={}
    for s in arr:
        if s in freq:
            freq[s]+=1
        else:
            freq[s]=1
    for k,v in freq.items():
        if v>1:
            repeated[k]=v
    return repeated
arr=['banana','apple','mango','apple','banana']
print(repeat_check(arr))