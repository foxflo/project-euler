#What is the largest n-digit pandigital prime that exists?

""" The sum of the digits 1-9 is 45
                          1-8    36
                          1-7    28
                          1-6    21
                          1-5    15
                          1-4    10
                          1-3    6
                          1-2    3
                          1-1    1
                          
    Thus, we do not need to check when n=1,2,3,5,6,8,9 for primes since all these digit sums are 3 which means
    any n pandigital number where n=1,2,3,5,6,8,9 will be divisible by 3 and thus not prime. So we only need 
    to check 4 and 7 digit panditigal numbers.
    
    There are 7!=5040 7 digit pandigital numbers and 4!=24 pandigital numbers.
    
    It might be faster to cache primes first, but there are so few to check that we shouldn't really
    notice the difference between caching and brute force test division. 
    
    We use factoradic for easy enumeration of the permutations in normal integer order by way of the Lehmer code.
"""

from util import toFactoradic, isPrime

def p41():
    #enumerate 7 digit pandigitals in decreasing order
    for i in xrange(5039,-1,-1):
        factoradic=toFactoradic(i,6)
        array=[str(i) for i in xrange(1,8)]
        permutation=''
        for j in factoradic:
            permutation+=array[int(j)]
            del array[int(j)]
        if isPrime(int(permutation)):
            print permutation
            return
    #enumerate four digit pandigitals in decreasing order
    for i in xrange(23,-1,-1):
        factoradic=toFactoradic(i,3)
        array=[str(i) for i in xrange(1,5)]
        permutation=''
        for j in factoradic:
            permutation+=array[int(j)]
            del array[int(j)]
        if isPrime(int(permutation)):
            print permutation
            return
p41()
