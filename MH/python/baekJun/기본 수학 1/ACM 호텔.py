T=int(input())
for i in range(T) :
    H,W,N=map(int,input().split())
    col=N//H+1
    row=N%H
    if N%H==0 :
        col-=1
        row=H

    print(row*100+col)