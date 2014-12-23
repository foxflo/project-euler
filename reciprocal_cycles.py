#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

""" The wikipedia entry on repeating decimals says that for the unit fraction 1/d, the maximum length the 
    recurring cycle could be is d-1. Since if 0 occurs as a remainder, we are done. So if the decimal is
    repeating, 0 cannot occur. This leaves d-1 choices and eventually one must repeat at which point
    the sequence repeats. That is, if we see a remainder more than once, then the cycle repeats there
    
    Thus, we can check from the top and whenever we find a d' such that 1/d' has length d'-1, we can be sure that
    no repeating decimal with d < d' has a larger repetition length.
    
    Furthermore, our check works because all unit fractions must either terminate or repeat when represented
    as a decimal.
"""

""" Compute whether the unit fraction 1/n terminates
"""
        
def terminates(n):
    while n%5==0:
        n/=5
    while n%2==0:
        n/=2
    if n==1:
        return True
    return False

def p26(n=1000):
    max_length=(0,0)
    for i in xrange(n,0,-1):
        if terminates(i):
            continue
        seen_remainders=[False]*i
        counter=1
        remainder=1
        while not seen_remainders[remainder]:
            seen_remainders[remainder]=counter
            remainder=10*remainder%i
            counter+=1
        if counter-seen_remainders[remainder] > max_length[0]:
            max_length=(counter-seen_remainders[remainder],i)
        if counter-seen_remainders[remainder] == i-1:
            break
    print max_length[1]
p26()
