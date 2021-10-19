M=int(input())
N=int(input())

r=list(map(int,range(M,N+1)))
def identify_decimal(k) :
    if k==1 :
        return 0
    for i in range(2,k+1) :
        if k==i :
            return 1
        elif k%i==0 :
            return 0
decimals=list(map(int,((k*identify_decimal(k))for k in r)))
if sum(decimals)==0 :
    print(-1)
else :
    print(sum(decimals))
    while 1 :
        try :
            decimals.remove(0)
        except :
            break
    print(min(decimals))
        