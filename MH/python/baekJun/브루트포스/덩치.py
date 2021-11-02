N=int(input())
weight,height=[],[]
for i in range(N) :
  a,b=map(int,input().split())
  weight.append(a)
  height.append(b)

# height=[110, 230, 120, 210, 160, 180]
# weight=[10, 48, 32, 22, 60, 72]
# N=6

rank=[1]*N

for i in range(N) : # 55 i는 지금 검사 중인 대상
  for j in range(N) : # 55, 58, 88, 60 ,46, 32 j는 i와 비교할 대상
    if weight[j]>weight[i] and height[j]>height[i] :
      rank[i]+=1

str_rank=str(rank[0])
for i in range(1,N) :
  str_rank+=" "
  str_rank+=str(rank[i])

print(str_rank)
# 밑의 방식으로 백준에 제출하면 안 됨.
# print(*map(int,"".join(map(str,rank))))

