from math import *

A,B,V=map(int,input().split())
planA=ceil((V-A)/(A-B))+1
print(planA)

go=0
count=0
while 1 :
    go+=A
    count+=1
    if go>=V :
        break
    go-=B
planB=count
print(planB)