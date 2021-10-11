N=int(input())

n,j=2,0
if N==1 :
    print(1)
else :
    while 1:
        j+=1
        k=5+6*(j-1)
        d=6*j
        #print("j=%d k=%d d=%d n=%d %d~%d"%(j,k,d,n,n,n+k))
        if N>=n and N<=n+k :
            print(j+1)
            break
        n+=d


