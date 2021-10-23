x,y=[],[]
for k in range(3) :
  a,b=map(int,input().split())
  x.append(a)
  y.append(b)
for i in x :
  if x.count(i)==1 :
    px=i
for j in y :
  if y.count(j)==1 :
    py=j
print(px,py)