# https://leedakyeong.tistory.com/entry/python-for%EB%AC%B8-if%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0

#10부터 20까지 list에 저장
l=[i for i in range(10,21)]
l=list(range(10,21))
print(l)
# 중첩 for문 한 줄
for a in b :
    for c in a :
        print(c)
for a in b for c in a : print(c)
# if문 한 줄
v=3
if v<5 : print(0)
# 5이상이면 1을 출력하고 싶을 때
print(0 if v<5 else 1)
# 여러 조건
if v<5 :
    print(0)
elif v<10 :
    print(1)
else :
    print(2)
print(0 if v<5 else 1 if v<10 else 2)