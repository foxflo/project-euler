#What 12-digit number do you form by concatenating the three terms in this sequence?

from math import ceil
from util import toFactoradic

def p49():
    #Generate all four digit primes
    primes=[2]
    counter=0   #record the index of the first four digit prime
    for i in xrange(3,9999):
        upper_lim=int(ceil(i**0.5))
        add=False
        for j in primes:
            if j>upper_lim or j==primes[-1]:
                add=True
                break
            if i%j==0:
                break
        if add:
            add=False
            if not counter and len(str(i)) > 3:
                counter=len(primes)
            primes.append(i)
    primes=set(primes[counter:])
    
    #generate all permutation sets of primes with more than two elements
    prime_permutations=[]
    
    while primes:
        candidate=primes.pop()
        permutations=[candidate]
        for i in xrange(23,-1,-1):
            factoradic=toFactoradic(i,3)
            array=[str(i) for i in str(candidate)]
            permutation=''
            for j in factoradic:
                permutation+=array[int(j)]
                del array[int(j)]
            permutation=int(permutation)
            if permutation in primes:
                permutations.append(permutation)
                primes.remove(permutation)
        if len(permutations)>2:
            permutations.sort()
            for i in xrange(len(permutations)-2):
                differences=[permutations[j]-permutations[i] for j in xrange(i+1,len(permutations))]
                for j in xrange(len(differences)):
                    for k in xrange(j+1,len(differences)):
                        if 2*differences[j]==differences[k]:
                            prime_permutations.append((permutations[i],permutations[i]+differences[j],permutations[i]+differences[k]))
    print prime_permutations   
p49()
