word=input()
L=""
for i in range(len(word)) :
    L+=str(i)
trans=str.maketrans(word,L)
alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet=alphabet.translate(trans)
print(alphabet)