A,B,C=map(int,input().split())

if B!=C :
    BREAK_EVEN=int(A/(C-B)+1)
    if BREAK_EVEN<0 :
        print(-1)
    else :
        print(BREAK_EVEN)
else :
    print(-1)
