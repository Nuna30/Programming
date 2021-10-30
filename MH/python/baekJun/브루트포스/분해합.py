def plus(l) : # l=[1,2,2]
  str_l=""
  for i in l :
    str_l+=str(i)
  int_l=int(str_l)
  int_l+=1
  str_l=str(int_l)
  k=[]
  for i in range(len(l)-len(str_l)) :
    k.append(0)
  for i in str_l :
    k.append(int(i))
  return k,int_l

N=int(input())
n=len(str(N))
b=0

if N<=10 :
  if N%2==0 :
    print(int(N/2))
  else :
    print(0)

else :
  im,measure=0,0
  while 1 :
    measure+=(10**im+1)*9 # measure=18,117,...
    if measure > N :
      measure-=(10**im+1)*9
      break
    im+=1

  # print(im,measure)
  Mfactor=(10**im+1) # factor=2,11,101,1001,...,Mfactor
  imf=0
  while 1 :
    start_point=N-(measure+Mfactor*imf)
    if start_point<0 :
      break
    imf+=1 # [imf,0,0]부터 시작

  a=[0]*n
  a[-im-1]=imf

  while 1:
    Sum,Index=0,0
    for i in range(n-1,-1,-1) :
      Sum+=(10**i+1)*a[Index]
      Index+=1
    # print(a,Sum)
    if Sum==N :
      sol=""
      for i in a :
        sol+=str(i)
      print(int(sol)) #
      break
    elif Sum>N and b>N :
      print(0) #
      break
    a,b=plus(a)


# 다른 사람 꺼...
# a = int(input())
# if a < len(str(a))*9 :
#     b = 0
# else : b = a - len(str(a))*9

# for i in range(b, a) :
#   if sum(map(int, list(str(i)))) + i == a :
#     print(i)
#     break
#   if i == a-1 :
#     print(0)
#     break
# 요약하면 a가 32일 때
# b부터 검사해서 (b가 25라면) 25+2+5를 해서 32이면 답으로 간주하는 방식
# b 설명 :
# a가 21일 때
# b는 3이다. 0부터 시작하긴 힘드니까 abcd+a+b+c+d에서 각 자리를 더하는 부분의 ㅊ최대값 9*len
# 을 a에서 빼고 시작하는 것 같다.
# 시작 기준이 대충이어도 시간이 적게 걸리면 그만이다.
