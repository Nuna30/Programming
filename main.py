

# 다른 사람 꺼...
while 1:
  a = int(input())
  if a < len(str(a))*9 :
      b = 0
  else : b = a - len(str(a))*9

  print(b)
  for i in range(b, a) :
    if sum(map(int, list(str(i)))) + i == a :
      print(i)
      break
    if i == a-1 :
      print(0)
      break
      
# 요약하면 a가 32일 때
# b부터 검사해서 (b가 25라면) 25+2+5를 해서 32이면 답으로 간주하는 방식
# b 설명 :
# a가 21일 때
# b는 3이다. 0부터 시작하긴 힘드니까 abcd+a+b+c+d에서 각 자리를 더하는 부분의 ㅊ최대값 9*len
# 을 a에서 빼고 시작하는 것 같다.
# 시작 기준이 대충이어도 시간이 적게 걸리면 그만이다.

