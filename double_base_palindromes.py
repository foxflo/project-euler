#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

""" Since leading zeroes cannot be included, we need to exclude all numbers that are multiples of 10 and 2.
    This is equivalent to excluding all numbers that are multiples of 2.
"""

from util import isPalin

def p36(n=1000000):
    total=0
    for i in xrange(1,n,2):
        if isPalin(str(i)) and isPalin(bin(i)[2:]):
            total+=i
    print total
p36()

