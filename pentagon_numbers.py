#Find the pair of pentagonal numbers, P_j and P_k, for which their sum and difference are pentagonal and D = |P_k - P_j| is minimised; what is the value of D?

""" I tried finding a clever solution but it seems none exists.
    
    The algorithm is as follows:
        
    compute the nth (starting from the 2nd) pentagonal number. Consider the differences and sums for the nth number
    and all pentagonal numbers below it (starting from the top). Then the first number we find with a 
    pentagonal sum and difference must have the smallest such difference. 
    
    The only way  to verify this using this algorithm is to check until the next such pair is also found.
    
    Then since the difference between successive pentagonal numbers only increases, this will serve as
    verification that we have found the smallest.
    
    The test is truncated since it takes quite a while to find the next satisfying pentagonal number.
    In other words: got lucky! and essentially this works because satisfying pentagonal numbers are very rare.
"""

from util import isPentagonal

def p44():
    pentagonals=[1]
    i=2
    while True:
        current=i*(3*i-1)/2
        for j in xrange(1,i):
            if isPentagonal(current-pentagonals[j-1]) and isPentagonal(current+pentagonals[j-1]):
                print current-pentagonals[j-1]
                return
        pentagonals.append(current)
        i+=1
p44()
