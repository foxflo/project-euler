#Find the sum of all 0 to 9 pandigital numbers with this property.

from util import toFactoradic

""" Better yet, we could compute all three digit multiples of 17,13,11, etc. and find the ones which have the same
    shared digit. This isn't a complete algorithm, but it's an idea.
"""

primes=[2,3,5,7,11,13,17]

def p43():
    total=0
    for i in xrange(3628799,362879,-1):
        factoradic=toFactoradic(i,9)
        array=[str(i) for i in xrange(10)]
        permutation=''
        for j in factoradic:
            permutation+=array[int(j)]
            del array[int(j)]
        if not sum([int(permutation[j:j+3])%primes[j-1] for j in xrange(1,8)]):
            total+=int(permutation)
    print total
p43()
