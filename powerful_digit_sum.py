#Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

""" Yay arbitrary precision integer types.
"""

def p56(n=100):
    max_digit_sum=0
    for a in xrange(n):
        for b in xrange(n):
            max_digit_sum=max(max_digit_sum,sum(int(digit) for digit in str(a**b)))
    print max_digit_sum
p56()
