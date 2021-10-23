x,y,w,h=map(int,input().split())
ux,dx,uy,dy=w-x,x,h-y,y
p=[ux,dx,uy,dy]
print(min(p))