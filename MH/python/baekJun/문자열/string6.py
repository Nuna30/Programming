sentence=input()

spaces=sentence.count(" ")
if sentence[0]==" " :
    spaces-=1
if sentence[-1]==" " :
    spaces-=1

print(spaces+1)
