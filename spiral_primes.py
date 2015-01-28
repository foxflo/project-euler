#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

""" Since the 1x1 grid has a 0% prime ratio, we will ignore it as an edge case. 
"""

from util import isPrime

def p58(n=0.10):
    corners=[3,5,7]
    #upper right, upper left, lower left, lower right is never prime
    differences=[10,12,14]
    #Notice that as the grid expands one rotation, all these differences increase by 8 every time
    statistics=[3,3,5]
    #current side length, currrent number of primes, total number of corners
    while statistics[1]/(statistics[2]+0.0) > n:
        corners=[corners[i]+differences[i] for i in xrange(3)]
        differences=[i+8 for i in differences]
        update=[2,sum([int(isPrime(i)) for i in corners]),4]
        statistics=[statistics[i]+update[i] for i in xrange(3)]
    print statistics[0]
p58()
