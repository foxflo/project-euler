#How many n-digit positive integers exist which are also an nth power?

""" We could keep checking numbers forever if we just naively brute force. To stop this, note that we need numbers
    such that 10^(n-1) <= d^n < 10^n i.e. x^n has n digits. 
    
    But in order for x^n < 10^n to be true, x must then be strictly less than 10 (i.e. an integer 1-9). 
    Furthermore, we want some bound for n when x^n >= 10^(n-1). If we can't bound n, then we'll just keep checking
    forever, which means the program could never terminate.
    
    Taking the nth root of both sides of the inequality yields x >= 10^((n-1)/n). But as n grows large, 
    10^((n-1)/n) becomes larger than 9 and we know we are done since the upper bound on x is 9 (inclusive).
    
    Then we just solve 9=10^((n-1)/n) for n to get n~~21.852 so we'll check up to n=22.
"""

def p63():
    total=0
    for x in xrange(1,10):
        for n in xrange(1,23):
            if len(str(x**n))==n:
                total+=1
    print total
p63()
