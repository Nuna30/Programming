# 분해합과 생성자 과정을 print 해줌.
i=1000
while 1:
  if i>100000 :
    break
  sum=i
  L=""
  sL=[i,i]
  count=0
  for j in str(i) :
    sum+=int(j)
    count+=1
    sL.append(int(j))
  sL.append(sum)
  L+=("%d -> %d + ")
  for i in range(count-1) :
    L+=("%d + ")
  L+=("%d -> %d")
  i=sum
  sL=tuple(sL)
  print(L%sL)