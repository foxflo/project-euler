#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

""" Thank Guido for implicit arbitrary precision integer arithmetic.
"""

def p48(n=1000):
    sum=0
    for i in xrange(1,n+1):
        sum+=i**i
    print str(sum)[-10:]
p48()
