M,N=map(int,input().split())
prime=[2]
p=0
for i in range(2,N+1) :
    # print("i",i)
    for j in prime :
        if i<=j*2 :
            if i%j==0 :
                print("i",i,"j",j)
                p=0
                break
            if i%j!=0 and j==prime[-1] :
                prime.append(i)
                # print("j",j)
                print(prime)
                p=1
                break
    # print(p)
    if i>=M and i<=N and p==1 :
        print(i)
        p=0