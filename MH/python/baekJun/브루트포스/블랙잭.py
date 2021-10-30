N,M=map(int,input().split())
cards=list(map(int,input().split()))
cards.sort()
sum=[]
for i in range(0,len(cards)) :
  for j in range(i+1,len(cards)) :
    for k in range(j+1,len(cards)) :
      if cards[i]+cards[j]+cards[k]>M :
        break
      # print("%d+%d+%d"%(cards[i],cards[j],cards[k]))
      sum.append(cards[i]+cards[j]+cards[k])

print(max(sum))