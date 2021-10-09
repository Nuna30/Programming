def d(n) :
    N=list(map(int,str(n)))
    return n+sum(N)
n=1
k=0
while n<10000 :
    if n>=9 :
        n+=11
        k+=1
        if k>9 :
            k=0
            n-=9
    else :
        n+=2