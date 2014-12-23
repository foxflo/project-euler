#What is the value of the first triangle number to have over five hundred divisors?

from util import numDivisors

def p12(n=500):
    num_divisors=0
    counter=1
    while num_divisors <= n:
        num_divisors=0
        triang=counter*(counter+1)/2
        num_divisors=numDivisors(triang)
        counter+=1
    print triang
p12()
