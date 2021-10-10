words=input()
croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in croatia :
    if words.count(i)!=0 :
        words=words.replace(i,"1")

print(len(words))
