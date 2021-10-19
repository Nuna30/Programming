L=list(((int(input())%42+1)for i in range(10)))
S=[]
for i in range(10) :
    if S.count(L[i])==0 :
        S.append(L[i])
print(len(S))

