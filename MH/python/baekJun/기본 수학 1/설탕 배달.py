N=int(input())
a=N//5
멈춰=0
#print("a",a)
if 5*a==N :
    print(a)
else :
    for i in range(a,-1,-1) :
        #print("i",i)
        b=0
        while (i*5+b*3) <= N :
            #print("%d*5+%d*3"%(i,b))
            b+=1
            if i*5+b*3==N :
                print(i+b)
                멈춰=1
                break
        if 멈춰==1 :
            break
    if 멈춰==0 :
        print(-1)

