def d(n) :
    N=list(map(int,str(n)))
    return n+sum(N)

S=set()
A=set()
for i in range(1,10001) :
    S.add(d(i))

for i in range(1,10001) :
    A.add(i)

for i in sorted(A-S) :
    print(i)

