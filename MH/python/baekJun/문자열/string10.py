N=int(input())
count=0
for i in range(N) :
    apple=list(map(str,input())) #[h a p p p y z z a]
    #print("apple :",apple)
    banana=list(set(apple))#[h a p y z ]
    #print("banana :",banana)
    index=[]
    NO=0
    for a in banana : #[h a p y z ]
        inin=[]
        for b in range(len(apple)) :
            if apple[b]==a :
                inin.append(b)
        index.append(inin)
        #print("inin :",inin)
        #print("index :",index)
    for c in range(len(index)) :
        if len(index[c])!=1 :
            for d in range(len(index[c])-1) :
                #print("index[%d][%d] index[%d][%d]"%(c,d,c,d+1))
                if index[c][d]!=index[c][d+1]-1 :
                    NO=1
    if NO!=1 :
        count+=1
       #print("count")

print(count)


