from math import ceil,sqrt

""" Compute whether a number is pentagonal

    To check whether a number, x, is pentagonal, we need to see whether it can be written as:
    x=n(3n-1)/2. Solving this equation for n yields: n=1/6(1+/- sqrt(1+24x)). However, the smaller root is 
    negative and since there are no negative pentagonal numbers, we only need to take the positive
    root. Then to check whether x is pentagonal, we need to see whether it gives an integral result for n.
"""
def isPentagonal(n):
    num=(1+sqrt(1+24*n))/6
    return int(num)==num

""" Compute whether a number is triangular
    Takes the same approach as above, except solve x=n(n+1)/2 and take the positive root.
"""
def isTriangular(n):
    num=(-1+sqrt(1+8*n))/2
    return int(num)==num

factorials={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
""" Compute the factoradic representation of a base 10 number, factorials is precomputed for table lookups
"""
def toFactoradic(n,num_digs):
    if n==0:
        return '0'*num_digs
    factoradic=""
    counter=num_digs #how many choices do we need to make
    while factorials[counter] > n:
        counter-=1
        factoradic+='0'
    while counter >= 0:
        temp=n/factorials[counter]
        n-=temp*factorials[counter]
        factoradic+=str(temp)
        counter-=1
    return factoradic

""" Determine whether a number has a repeating digit
"""
def repeatsDigits(n):
    digits=list(n)
    if len(set(digits)) != len(digits):
        return True

""" Determine whether a number is a palindrome
"""
def isPalin(n):
    return n==n[::-1]

""" Compute whether a number is prime or not
"""
def isPrime(n):
    if n==1:
        return False
    if n%2==0:
        return False
    elif n%3==0:
        return False
    else:
        for i in xrange(5, int(n**0.5),6):
            if n%i==0 or n%(i+2)==0:
                return False
    return True

""" Return a list of the pairs of divisors of a number (excluding 1, itself, and its square root)
"""
def getDivisors(n):
    divs=[]
    for i in xrange(2,int(ceil(n**0.5))):
        if n%i==0:
            divs.append((i,n/i))
    return divs

""" Compute the number of divisors of a number
"""    
def numDivisors(n):
    num=0
    for i in xrange(1,int(n**0.5)+1):
        if n%i==0:
            num+=2
    if int(n**0.5)**2==n:
        num-=1
    return num
   
""" Compute the sum of the proper divisors of a number
""" 
def sumDivisors(n):
    sum_divisors=1
    for j in xrange(2,int(n**0.5)+1):
        if n%j==0:
            sum_divisors+=j+n/j
    if int(n**0.5)**2==n:
        sum_divisors-=int(n**0.5)  
    return sum_divisors  
    
""" Compute n choose k
"""    
def choose(n,k):
    if k > n:
        return 0
    product=1
    ignores=max(k,n-k)
    rest=n-ignores
    for i in xrange(ignores+1, n+1):
        product*=i
    for i in xrange(1,rest+1):
        product/=i
    return product
    
""" Compute the gcd of two numbers
"""
def gcd(n,m):
    while m!=0:
        temp=m
        m=n%m
        n=temp
    return n
    
