A,B=map(str,input().split())

def r(num) :
    rev=""
    for i in range(len(num)-1,-1,-1) :
        rev+=num[i]
    return int(rev)

if r(A) > r(B) :
    print(r(A))
elif r(B) > r(A) :
    print(r(B))

