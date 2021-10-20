a=[i for i in range(2,1000001)]
b=2
while 1 :
    a.remove(2*b)
    b+=1
print(a)
