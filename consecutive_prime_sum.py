#Which prime, below one-million, can be written as the sum of the most consecutive primes?

from util import gen_primes_below_n,isPrime

def p50(n=1000000):
    primes=gen_primes_below_n(n)
    primeset=set(primes)
    num_primes=0
    initial=0
    for i in xrange(len(primes)):
        for j in xrange(i+1,len(primes)):
            temp=sum(primes[i:j])
            if temp > n:
                break
            if temp in primeset and j-i>num_primes:
                num_primes=j-i
                initial=i
    print sum(primes[initial:initial+num_primes])
p50()
