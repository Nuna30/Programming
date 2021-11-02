a=[1,2,3,4,5]
# a를 "12345" 로 만들고 싶으면

a="".join(map(str,a)) # 하면 된다.
print(a)