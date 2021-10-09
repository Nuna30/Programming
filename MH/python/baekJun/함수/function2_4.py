L=[]
for i in range(1,10001) :
    L.append(i)

for a in range(0,10) :
    for b in range(0,10) :
        for c in range(0,10) :
            for d in range(0,10) :
                if L.count(1001*a+101*b+11*c+2*d)!=0 :
                    L.remove(1001*a+101*b+11*c+2*d)
                    #print(a,b,c,d,"1001*a+101*b+11*c+2*d=%d"%(1001*a+101*b+11*c+2*d))
                else :
                    continue
print(L)
