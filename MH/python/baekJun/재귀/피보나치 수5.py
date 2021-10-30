def fibonacci(N) :
  if N==0 :
    return(0)
  elif N==1 :
    return(1)
  elif N==2 :
    return(1)
  elif N>=3 :
    return fibonacci(N-2)+fibonacci(N-1)

n=int(input())
print(fibonacci(n))

  