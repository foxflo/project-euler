#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from util import sumDivisors
from collections import defaultdict

def p23():
    x=[]
    for i in xrange(12,28123+1-12):
        sum_divs=sumDivisors(i)
        if sum_divs>i:
            x.append(i)
    abundant_sums=[False]*28124
    for i in xrange(len(x)):
        for j in xrange(i,len(x)):
            if x[i]+x[j] > 28123:
                break
            abundant_sums[x[i]+x[j]]=True
    total=0
    for i in xrange(len(abundant_sums)):
        if not abundant_sums[i]:
            total+=i
    print total
p23()
