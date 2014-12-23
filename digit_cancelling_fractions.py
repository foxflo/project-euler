#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from util import gcd

def p33(n=2):
    numerators=[]
    denominators=[]
    for i in xrange(10**(n-2),10**(n-1)):
        for j in xrange(10**(n-2),10**(n-1)):
            if i==j:
                continue
            for k in xrange(1,10):
                numerator=10*i+k
                denominator=j+10**(n-1)*k
                if numerator >= denominator:
                    continue
                if numerator/(denominator+0.0)==i/(j+0.0):
                    numerators.append(i)
                    denominators.append(j)
    numerator=reduce(lambda a,b:a*b,numerators)
    denominator=reduce(lambda a,b:a*b,denominators)
    divisor=gcd(numerator, denominator)
    numerator/=divisor
    denominator/=divisor
    print numerator,denominator
p33()
