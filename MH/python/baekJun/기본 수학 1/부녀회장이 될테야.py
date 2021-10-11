T=int(input())
for i in range(T) :
    k=int(input())
    n=int(input())
    L=[]
    S=[]
    for i in range(1,n+1) :
        L.append(i)
    S.append(L)
    for i in range(1,k+1) :
        L=[]
        L.append(1)
        for a in range(n-1) :
            #print("L.append(L[%d]+S[%d][%d])"%(a,i-1,a+1))
            L.append(L[a]+S[i-1][a+1])
        S.append(L)
    #print(S)
    print(S[-1][-1])
