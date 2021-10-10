word=input()
#word="UNUCIC"
word=list(map(str,word))
#word=['U', 'N', 'U', 'C', 'I', 'C']

alphabet=list(map(chr,range(ord("A"),ord("Z")+1)))
apple=[3,3,3,3,3,4,3,4]

def combine(a,b,L) :
    banana=""
    for i in range(a,b+1) :
        banana+=L[i]
    return banana

candy=[]
dolphin=0
for i in apple :
    candy.append(combine(dolphin,dolphin+i-1,alphabet))
    dolphin+=i

#candy=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ego=[]
for i in range(len(candy)) :
    ego.append(i+2)
    ego.append(list(map(str,candy[i])))
#ego=[2, ['A', 'B', 'C'], 3, ['D', 'E', 'F'], 4, ['G', 'H', 'I'], 5, ['J', 'K', 'L'], 6, ['M', 'N', 'O'], 7, ['P', 'Q', 'R', 'S'], 8, ['T', 'U', 'V'], 9, ['W', 'X', 'Y', 'Z']]

finale=0
for a in word :
    for b in range(1,len(ego),2) :
        if ego[b].count(a)!=0 :
            finale+=ego[b-1]+1
print(finale)
