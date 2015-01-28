#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

from collections import defaultdict

factorials=[1,1,2,6,24,120,720,5040,40320,362880]

def p74(n=1000000):
    cache=defaultdict(lambda:0)
    cache[1]=1
    for i in xrange(n):
        toAdd=[]
        temp=i
        while not cache[temp]:
            toAdd.append(temp)
            cache[temp]=-1
            temp=sum([factorials[int(j)] for j in  
        for i in xrange(len(toAdd)-1,-1,-1):
            cache[toAdd[i]]=
p74()
