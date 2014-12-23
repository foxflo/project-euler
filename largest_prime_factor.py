#What is the largest prime factor of the number 600851475143 

from util import isPrime

def p3(x=600851475143):
    below=[]
    for i in xrange(2,int(x**0.5)):
        if x%i==0:
            if isPrime(x/i):
                print x/i
                return
            below.append(i)
    for i in below[::-1]:
        if isPrime(i):
            print i
            return
    return x
p3()
