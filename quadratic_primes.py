#Find the product of the coefficients,a and b,for the quadratic expression that produces the maximum number of primes for consecutive values of n,starting with n = 0.

""" Whenever n=b, n^2+an+b is divisible by b. Thus, the number of consecutive primes is bounded by b.

    Furthermore, since we produce 40 primes for n^2+n+41, which is the maximum number of primes possible, 
    we only need to check b > 41. 
    
    Furthermore,we only need to check prime b since if b is not prime, then when n=0,n^2+an+b is not prime, 
    and we can not have consecutive primes beginning with n=0.
    
    Finally, since b>41 and b is prime, b must be odd. when n=1, for n^2+an+b = 1+a+b to be prime, a must be odd. 
    
    We ignore negative numbers since by the strictest definition cannot be negative since they are divisible by
    numbers other than 1 and itself (namely -1 and the negative of itself).
"""

from util import isPrime

#possible values for b
primes=[43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

""" Note: problem not solved in general, but could be made to do so by generating primes until the desired
    limit is reached.
"""

def p27():
    max_consecutive_primes=40
    pair=(1,41) #store the a and b values
    for b in primes:
        for a in xrange(-999,1000,2):
            consecutive_primes=1
            for n in xrange(1,b):
                num=n*n+a*n+b
                if num < 0:
                    break
                if isPrime(num):
                    consecutive_primes+=1
                else:
                    break
            if consecutive_primes > max_consecutive_primes:
                pair=(a,b)
                max_consecutive_primes=consecutive_primes
    print pair, pair[0]*pair[1]
p27()
