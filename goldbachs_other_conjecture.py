#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import sqrt,ceil

def p46():
    primes=[2]
    counter=3
    while True:
        upper_lim=int(ceil(counter**0.5))
        add=False
        for j in primes:
            if j>upper_lim or j==primes[-1]:
                add=True
                break
            if counter%j==0:
                break
        if add:
            add=False
            primes.append(counter)
        else:
            counterExample=True
            for j in primes[1:]:
                num=(counter-j)/2
                if int(sqrt(num))==sqrt(num):
                    counterExample=False
                    break
            if counterExample:
                print counter
                return
        counter+=2
p46()
