N=int(input())
N0=N
n=0
while 1:
    n+=1
    s=N//10+N%10
    N=N%10*10+s%10
    if N0==N :
        print(n)
        break
