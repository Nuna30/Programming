N,A=map(int,input().split())

series=list(map(int,input().split()))
r_series=""

for i in range(N) :
    if series[i]<A :
        r_series+=str(series[i])+" "

print(r_series)