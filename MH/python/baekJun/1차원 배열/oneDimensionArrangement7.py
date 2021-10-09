C=int(input())

for i in range(C) :
    L=list(map(int,input().split()))
    mean=sum(L[1:])/(len(L)-1)
    c=0
    for a in range(1,L[0]+1) :
        if L[a]>mean :
            c+=1
    print("%.3f%%"%(100*c/(len(L)-1)))