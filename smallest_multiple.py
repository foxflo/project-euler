#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from collections import defaultdict

def p5(n=20):
    factors=defaultdict(lambda:0)
    for i in xrange(2,n+1):
        tempFactors=defaultdict(lambda:0)
        for j in xrange(2,n+1):
            while i%j==0:
                i=i/j
                tempFactors[j]+=1
        for j in xrange(2,n+1):
            factors[j]=max(factors[j],tempFactors[j])
    smallest_num=1
    for factor,num_times in factors.items():
        smallest_num*=factor**num_times
    print smallest_num
p5()
