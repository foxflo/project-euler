#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

""" It turns out that a clever way to write down numbers (the factoradic base system) allows us to 
    number permutations lexicographically and generate them easily. This is the Lehmer code.
    
    Then we just need to convert one million minus 1 to factoradic and read off the correct permutation.
    Minus one since the factoradic numbering system starts from 0
"""

from util import toFactoradic

def p24(n=1000000):
    factoradic=toFactoradic(n-1,9)
    array=[str(i) for i in xrange(10)]
    permutation=''
    for i in factoradic:
        permutation+=array[int(i)]
        del array[int(i)]
    print permutation
p24()
