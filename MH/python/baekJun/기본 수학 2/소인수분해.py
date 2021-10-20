N=int(input())

decimal=2
while 1 :
    if N==1 :
        break
    if N%decimal==0 :
        print(decimal)
        N/=decimal
    else :
        decimal+=1