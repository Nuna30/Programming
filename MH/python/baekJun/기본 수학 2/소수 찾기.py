N=int(input())
decimal=list(map(int,input().split(" ")))
count=0
for i in range(N) :
    if decimal[i]==1 :
        continue
    k=2
    while 1 :
        if k==decimal[i] :
            count+=1
            break
        elif decimal[i]%k==0 :
            break
        k+=1
print(count)