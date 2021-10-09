def d(n) :
    N=list(map(int,str(n)))
    return n+sum(N)
# 1~10000 리스트 생성
L=[]
for i in range(1,10001) :
    L.append(i)

n0=1
while n0!=10000 :
    if L.count(n0) !=0 :
        n=n0
        while 1 :
            #print("d(%d)=%d"%(n,d(n)))
            n=d(n)
            if n>=10000 :
                break
            else :
                if L.count(n)!=0 :
                    L.remove(n)
    n0+=1

S=[]
for i in range(1,len(L)) :
    S.append(L[i]-L[i-1])
    

print(L)
print(S)
