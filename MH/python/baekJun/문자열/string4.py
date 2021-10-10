T=int(input())
S2=""
for i in range(T) :
    R,S=input().split()
    S=[*S]
    for i in range(len(S)) :
        S2+=str(S[i])*int(R)
    print(S2)
    S2=""
    
