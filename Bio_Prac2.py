# Find identity value of a give sequence

from __future__ import division
se1=raw_input("Enter the first Sequence::")
se2=raw_input("Enter the Second Sequence::")

seq1=list(se1)
seq2=list(se2)

def find_identity(a,b):
    gap(a,b)
    print(a)
    print(b)
    score=0
    length=len(a)
    total_elements=len(a)*len(b)
    for i in range(0,length):
        for j in range(0,length):
            if(a[i]==b[j]):
                score=score+1
    identity = (score/total_elements)*100
    print("Mactching Score::",score)
    print("Identity of the sequence ::",identity)

def gap(a,b):
    if(len(a)==len(b)):
        print('')
    else:
        k=int(input("Enter the position to insert gap::"))
        if(len(a)<len(b)):
            a.insert(k,'-')
        else:
            b.insert(k,'-')
    return(a,b)


find_identity(seq1,seq2)
