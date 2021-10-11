x=int(input())
row=0
n=1
while 1 :
    row+=1
    d=row-1
    #print("row",row,"d",d,"n",n)
    if x>=n and x<=n+d :
        if row%2==0 :
            s=row*(row-1)/2+1
        else :
            s=row*(row+1)/2
        f=abs(s-x)
        print("%d/%d"%((1+f),(row-f)))
        break
    n+=row
        