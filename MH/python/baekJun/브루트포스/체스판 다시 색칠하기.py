M,N=map(int,input().split())
# print("M,N",M,N)
board=[]
for _ in range(M) :
  board.append(list(i for i in list(input())))
# print("board",board)
sol=[]
for l in range(0,M-7) :
  # print("l",l)
  for j in range(0,N-7) :
    # print("j",j)
    c1,c2=0,0
    for k in range(l,l+8) :
      # print("k",k)
      for i in range(j,j+8) :
        # print("i",i)
        if (k+i)%2==0 :
          if board[k][i]!='B' :
            c1+=1
          else :
            c2+=1
        else :
          if board[k][i]!='W' :
            c1+=1
          else :
            c2+=1
    sol.append(min([c1,c2]))
print(min(sol))

