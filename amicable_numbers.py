#Evaluate the sum of all the amicable numbers under 10000.

from util import sumDivisors

def p21(n=10000):
    x=[None]*n
    for current_number in xrange(2,n):
        x[current_number]=sumDivisors(current_number)
    x[0],x[1]=0,0   #Edge cases for numbers with no proper divisors
    amicable_sum=0
    for i in xrange(len(x)):
        if x[i] < n and i==x[x[i]] and x[i]!=i:
            amicable_sum+=i
    print amicable_sum
p21()

