#How many starting numbers below ten million will arrive at 89?

""" In addition to caching results, we should probably also realize that all the permutations of the digits of
    a number have the same square digit sum as the number and not recalculate all of those. 
    
    As it is currently it's quite slow.
    
    Furthermore, it is important for correctness to note that no square digit sum of a number can have more 
    than 7 digits if the number is under 10,000,000
"""

from collections import defaultdict

def p92(n=10000000):
    cache=defaultdict(lambda:0)
    cache[1],cache[89]=1,89
    total=1
    for i in xrange(1,n):
        temp=i
        toCache=[temp]
        while not cache[temp]:
            temp=sum([int(i)*int(i) for i in str(temp)])
            toCache.append(temp)
        if cache[temp]==89:
            total+=len(toCache)-1
        for j in toCache:
            cache[j]=cache[temp]
    print total
p92()
