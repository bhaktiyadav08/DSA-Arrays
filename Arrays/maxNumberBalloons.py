txt="nlaebolko"
def maxNumberBalloons():
    d={}
    for t in txt:
        if t in d:
            d[t]+=1
        else:
            d[t]=1
    word='balloon'
    for w in txt:
        if w in word:
            d[w]-=1
        else:
            break
    

