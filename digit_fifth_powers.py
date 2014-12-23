#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

""" Single digit numbers do not count, as shown in the example.

    We need an upper bound to the number of numbers to check, otherwise we'll never find a correct algorithm.
    
    Consider 999,999. The sum of the fifth powers of its digits is 354294. The maximum sum attainable as
    the sum of the fifth powers of digits of a six-digit number is 354294. Then we certainly don't need to 
    check any numbers with more than six digits, since those numbers are too large to be the sum of the fifth
    powers of their digits. 
    
    In fact, the largest number we'll need to check is 354294. But we can do a better job on the bound, since the
    number that produces the maximum digit fifth power sum below 354294 is 299999, whose fifth power digit sum is
    295277. Repeating this argument, with the maximumm digit fifth power sum below 295277 being 199999, we find
    we can tighten the bound to 295246.
"""


""" Note: this problem could be optimized more for general n by iterating through the procedure above.
    (but as it is runs pretty quickly for modest n).
"""

def p30(n=5):
    limit=None
    if n==5:
        limit=295246
    else:
        power=9**n
        counter=1
        while counter*power > 10**counter-1:
            counter+=1
        limit=(10**counter-1)/10
        while counter*power > limit:
            limit+=10**(counter-1)
        limit-=10**(counter-1)
    total=0
    for i in xrange(10, limit):
        if sum([int(j)**n for j in  str(i)])==i:
            total+=i
    print total
p30(4)
