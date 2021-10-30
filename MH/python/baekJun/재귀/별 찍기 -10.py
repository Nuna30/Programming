def star(n) :
  if n==3 :
    return "***\n* *\n***"
  else :
    dn=int(n/3) 
    a=star(dn).split("\n")
    for i in range(a.count("")) :
      a.remove("")
    b=""
    for j in range(3) :
      if j%2==0 :
        for i in range(len(a)) :
          b+=a[i]*3
          b+="\n"
      else :
        for i in range(dn) : 
          for k in range(3) : 
            if k%2==0 :
              b+=a[i]
            else :
              b+=" "*dn
          b+="\n"
    return b

    
print(star(int(input())))