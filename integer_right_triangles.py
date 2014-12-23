#For which value of p <= 1000, is the number of solutions maximised? p is the perimeter of a right triangle with integral side lengths.

""" With euclid's formula (a=m^2-n^2, b=2mn, c=m^2+n^2) we can generate all pythagorean triples. 
    When we know the perimeter, we get the restriction p = a+b+c = m^2-n^2+2mn+m^2+n^2 = 2m(m+n).
    Thus we can see that p needs to be even and intuitively the more divisors p has, the larger the 
    number of solutions.
    
    Furthermore, we need that m > n, so we must be selective about the divisors we choose. In particular, we need
    to exclude 1, the number itself, and its square root (if it is integral). In addition, for any p, we have
    p = 2m(m+n). So either 2m and m+n or m and 2m+2n must multiply to p. Since m,n > 0, we know that m+n > m. 
    Then m+n must sum to the larger divisor of a pair and m must be the smaller divisor. But m must be larger
    than n. Thus, we only take pairs of divisors (d1,d2) where d1*d2=p/2 and d1 < d2.
    
    m=d1, n=d2-d1 and 2d1 > d2
"""

from util import getDivisors,gcd

def p39(n=1000):
    max_p=0
    max_solutions=0
    for i in xrange(4,n+1):
        num_solutions=0
        divs=getDivisors(i/2)
        k=[1,i/2]
        primitives=set()
        for pair in divs:
            k+=[pair[0],pair[1]]
        for j in k:
            divs=getDivisors(i/2/j)
            for pair in divs:
                if 2*pair[0] > pair[1]:
                    primitive=sorted([2*pair[0]*(pair[1]-pair[0]),pair[0]**2-(pair[1]-pair[0])**2])
                    temp=gcd(primitive[0],primitive[1])
                    primitive=(primitive[0]/temp,primitive[1]/temp)
                    primitives.add(primitive)
        if len(primitives) > max_solutions:
            max_solutions = len(primitives)
            max_p=i
    print max_p
p39()
