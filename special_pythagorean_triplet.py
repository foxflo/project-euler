#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

""" We know from Euclid's formula that we can generate pythagorean triples using the formulae:
    a=m^2-n^2
    b=2mn
    c=m^2+n^2
    for positive m and n where m > n
    
    If a+b+c=x, then simplifying yields 2m(m+n)=x ==> m(m+n) = x/2

    Note: This only works for x such that there is only one triple, as stipulated in the problem statement. 
    A more general solution is given in the solution to problem 39.
"""

def p9(x=1000):
    below = []
    above = []
    for i in xrange(1, int(x**0.5)):
        if x%i==0:
            below.append(i)
            above=[x/i]+above
    factors=below+above
    for factor in factors:
        temp=x/(2*factor)-factor
        if temp <= 0 or temp >= factor:
            continue
        print (factor**4-temp**4)*2*factor*temp
p9()
