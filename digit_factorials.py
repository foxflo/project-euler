#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

""" The largest number we need to consider is seven digits, since otherwise the number starts growing much
    faster than 9!*n, where n is the number of digits in the number.
    
    In particular, 9!*7=2540160. The largest sum we can achieve under this number is 1,999,999, whose factorial
    sum is 2177281. This serves as our upper bound.
"""

factorials=[1,1,2,6,24,120,720,5040,40320,362880]

#factorials of the numbers 0 through 9

def p34():
    total=0
    for i in xrange(10,2177282):
        temp=i
        for j in str(i):
            temp-=factorials[int(j)]
        if not temp:
            total+=i
    print total            
p34()
