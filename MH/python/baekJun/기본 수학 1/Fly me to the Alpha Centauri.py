import math
T=int(input())
for i in range(T) :
    x,y=map(int,input().split())
    n=y-x
    k=round(math.sqrt(n))
    내일휴가나간다=0
    if k**2<n :
        내일휴가나간다=1
    print((k-2)*2+3+내일휴가나간다)
