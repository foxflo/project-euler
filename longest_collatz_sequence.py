#Which starting number, under one million, produces the longest collatz chain?

from collections import defaultdict

chains=defaultdict(lambda:0)
chains[1]=1

def p14(n=1000000):
    max_chain=0
    max_length=0
    for i in xrange(1,n):
        temp_length=collatz(i)
        if temp_length > max_length:
            max_length=temp_length
            max_chain=i
    print max_chain
    
def collatz(n):
    if chains[n] != 0:
        return chains[n]
    if n%2==0:
        chains[n]=collatz(n/2)+1
        return chains[n]
    else:
        chains[n]=collatz(3*n+1)+1
        return chains[n]
        
p14()
