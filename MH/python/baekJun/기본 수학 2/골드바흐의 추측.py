prime_list=[True]*9999 # 0~9998
for i in range(2,int(9998**0.5)+1) :
    if prime_list[i]==True :
        for j in range(2*i,9998+1,i) :
            prime_list[j]=False
del prime_list[:2]
count=0
for k in prime_list :
    if k==True :
        prime_list[count]=count+2
    count+=1
for l in range(prime_list.count(False)) :
    prime_list.remove(False)
T=int(input())
for t in range(T) :
    N=int(input())
    n=N
    count=0
    for i in prime_list :
        if i>n-2 :
            n=count-1
            break
        count+=1
    prime=prime_list[:n+1]
    if len(prime)%2==0 :
        addr=int(len(prime)/2)
        times=addr
    else :
        addr=int(len(prime)/2)
        times=addr+1
    for i in range(times) :
        if prime.count(N-prime[addr])==1 :
            if N-prime[addr]<prime[addr] :
                print("%d %d"%(N-prime[addr],prime[addr]))
            else :
                print("%d %d"%(prime[addr],N-prime[addr]))
            break
        addr+=1

