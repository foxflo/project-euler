#How many circular primes are there below one million?

from math import ceil

def p35(n=1000000):
    primes=[2]
    circular_primes=0
    for i in xrange(3,n):
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
            primes.append(i)
    primes=set(primes)
    while primes:
        i=str(primes.pop())
        popped=set([int(i)])
        counter=1
        for j in xrange(1,len(str(i))):
            i=i[-1]+i[:-1]
            if int(i) in primes:
                counter+=1
                primes.remove(int(i))
                popped.add(int(i))
            elif int(i) in popped:
                pass
            else:
                counter=0
                break
        circular_primes+=counter
    print circular_primes
p35()
