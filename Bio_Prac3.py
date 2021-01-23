#Find similarity value of given sequences

from __future__ import division

sequence_one=raw_input("Enter the first sequence::")
sequence_two=raw_input("Enter the Second sequence::")
how_many=int(input("How many elements for similarity condition?"))
similarities=[]
for i in range(0,how_many):
    a=raw_input("Enter an element: ")
    c=int(input("How many elements is it similar to"))
    similarities.append([])
    similarities[i].append(a)

    for j in range (0,c):
        b=raw_input("What is it similar to?")
        similarities[i].append(b)

def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(o)):
        for j in range(len(s)):

            if o[i] in s[j] and t[i] in s[j] and o[i]!=t[i]:
                score+=1

        #calculating similarity
                similarity = (score*100)/len(o)
                return similarity


print(compare(list(sequence_one),list(sequence_two),similarities),"%")

      
