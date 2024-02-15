articles=["the","a","of","on"]
subj=["cat", "dog", "man", "woman"]
verbs=["sang", "ran", "jumped"]
adv=["loudly","quiet", "well", "badly"]
i=0
x=0


poem=("")
words=[articles,subj,verbs,adv]
sentence=("")

lines=int(input("how many lines?"))

import random

while x<lines:
    sentence=("")
    len=random.randint(2,3)
    while i<=len:
        sentence+=random.choice(words[i])+" "
        i+=1
    print(sentence)
    x+=1
    i=0
