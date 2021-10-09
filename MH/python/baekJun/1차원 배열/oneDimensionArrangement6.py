T=int(input())
L=list(input()for i in range(T))
for i in range(T) :
    n=0
    k=0
    for b in L[i] :
        if b=='O' :
            n+=1
            k+=n
        else :
            n=0
    print(k)
