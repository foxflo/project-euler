#Find the sum of all the multiples of 3 or 5 below 1000.

def p1(n=1000):
    print reduce(lambda a,b:a+b,[-15*(i+1) for i in xrange(n-1/15)]+[3*(i+1) for i in xrange(n-1/3)]+[5*(i+1) for i in xrange((n-1)/5)])
p1()
