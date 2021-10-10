N=int(input())
count=0
STOP=0
for i in range(1,N+1) :
    L=list(map(int,str(i)))
    minus_L=[]
    for b in range(1,len(L)) : # b=1,2
        minus=L[b]-L[b-1] # minus=4-2, 6-4
        minus_L.append(minus) # minus_L=[2,2]
    for c in range(len(minus_L)-1) : # c=0
        if minus_L[c]!=minus_L[c+1] :
            STOP=1
    if STOP==1 :
        STOP=0
        continue
    count+=1

print(count)