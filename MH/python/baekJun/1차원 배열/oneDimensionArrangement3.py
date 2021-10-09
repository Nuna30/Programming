A,B,C=map(int,(input()for i in range(3)))
s=list(str(A*B*C))
for i in range(10) :
    print(s.count(str(i)))