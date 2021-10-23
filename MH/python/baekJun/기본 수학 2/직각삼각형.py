while 1:
  a,b,c=map(int,input().split())
  if a==0 :
    break
  p=[a,b,c]
  C=max(p)
  del p[p.index(C)]
  A,B=p[0],p[1]
  if A**2+B**2==C**2 :
    print("right")
  else :
    print("wrong")