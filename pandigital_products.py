#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

""" The product can contain at most 7 digits. (If it contained more, we would not have enough digits to
    write any factors at all. But upon closer inspection, the product cannot contain more than four digits.
    
    For suppose it did. Then it must have at least 5 digits, and the divisors must total at most 4 digits.
    But then the maximum product we could produce would be only 4 digits, which is not enough to be the
    actual product. Thus, the product contains four or less digits.
    
    Actually, the product cannot contain fewer than four digits. For suppose it did. Then the product has at most
    3 digits while the divisors total at least 6 digits. But then the product could not have three or fewer
    digits, so ***the product must contain exactly four digits.***
"""

from util import getDivisors,repeatsDigits
        
def p32():
    total=0
    for i in xrange(1000,10000):
        if not repeatsDigits(str(i)) and '0' not in str(i):
            divs=getDivisors(i)
            for pair in divs:
                temp=str(pair[0])+str(pair[1])+str(i)
                if len(temp) == 9 and '0' not in temp and not repeatsDigits(temp):
                    total+=i
                    break
    print total
p32()
