N=int(input())
L=list(map(int,input().split()))
S=[]
for i in range(N) :
    S.append(L[i]/max(L)*100)
print(sum(S)/len(S))