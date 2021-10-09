L=[]
for i in range(9) :
    L.append(int(input()))

print(max(L),L.index(max(L))+1)