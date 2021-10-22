prime_list=[True]*(2*123456+1)
E=int(2*123456**0.5)
for a in range(2,E+1) :
    if prime_list[a]==True :
        for b in range(2*a,2*123456+1,a) : 
            prime_list[b]=False
while 1:
    n=int(input())
    if n==0 :
        break
    print(prime_list[n+1:2*n+1].count(True))
