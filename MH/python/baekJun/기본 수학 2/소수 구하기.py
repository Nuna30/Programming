M,N=map(int,input().split())

prime_list=[True]*N # 1 2 3 4 5 6 7 8 9 10
prime_list[0]=False
for i in range(2,(int(N**0.5)+1)) :
    for j in range(2*i-1,N,i) :
        prime_list[j]=False
prime=1
for i in prime_list :
    if i==True and prime>=M and prime<=N :
        print(prime)
    prime+=1