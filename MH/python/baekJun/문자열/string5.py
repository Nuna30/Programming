word=[*input()]
word=list(map(ord,word))
# Efficient
# word=[69, 102, 102, 105, 99, 105, 101, 110, 116]
# 대문자 ascii range(65~91) 소문자 range(97~123)
word_comparing=word
for i in range(len(word)) :
    if word[i] < 97 :
        word_comparing[i]+=32

word_sample=list(set(word))
counting=[]
for i in word_sample :
    counting.append(word.count(i))
if counting.count(max(counting)) > 1 :
    print("?")
else :
    answer=word_sample[counting.index(max(counting))]
    if answer >= 97 :
        answer-=32
    print(chr(answer))