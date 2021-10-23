T=int(input())
for _ in range(T) :
  x1,y1,r1,x2,y2,r2=map(int,input().split())

  b=((x1-x2)**2+(y1-y2)**2)**0.5
  a=b-(r1+r2)

  if a>0 :
    print(0)
  elif a==0 :
    print(1)
  else :
    R=[r1,r2]
    r1,r2=min(R),max(R)
    if a>-2*r1 :
      print(2)
    elif a==-2*r1 :
      if a==-2*r2 :
        print(-1)
      else :
        print(1)
    else :
      print(0)
  


      

  
