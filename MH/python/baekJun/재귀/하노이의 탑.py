n=int(input())

def k(n) :
  if n==1 :
    return 1 
  else :
    return 2*k(n-1)+1
print(k(n))
def sym(n,list_movedPlate=[]) :
  if n==1 :
    return list_movedPlate.append(1)
  sym(n-1,list_movedPlate)
  list_movedPlate.append(n)
  sym(n-1,list_movedPlate)
  return list_movedPlate
if n==1 :
  print(1,3)
else :
  list_movedPlate=sym(n)
  trail=[1]*n
  plate_number=list(map(int,(i for i in range(1,n+1))))
  for i in list_movedPlate :
    now_plateIndex=plate_number.index(i)
    before=trail[now_plateIndex]
    if n%2==0 :
      if now_plateIndex%2==0 :
        trail[now_plateIndex]=trail[now_plateIndex]+1
        if trail[now_plateIndex]==4 :
          trail[now_plateIndex]=1
      else :
        trail[now_plateIndex]=trail[now_plateIndex]-1
        if trail[now_plateIndex]==0 :
          trail[now_plateIndex]=3
    else :
      if now_plateIndex%2==0 :
        trail[now_plateIndex]=trail[now_plateIndex]-1
        if trail[now_plateIndex]==0 :
          trail[now_plateIndex]=3
      else :
        trail[now_plateIndex]=trail[now_plateIndex]+1
        if trail[now_plateIndex]==4 :
          trail[now_plateIndex]=1
    after=trail[now_plateIndex]
    print(before,after)

# t = int(input())
# cnt = 2 ** t - 1



# def hanoi(t, start, end, mid):
#     if t == 1:
#         print(start, end)
#     else:
#         hanoi(t - 1, start, mid, end)
#         print(start, end)
#         hanoi(t - 1, mid, end, start)

# print(cnt)
# hanoi(t, 1, 3, 2)