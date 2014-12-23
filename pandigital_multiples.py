#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

""" Note that the number n that we start with cannot have five  or more digits. If it did, then the concatenation
    would have 10 digits. However, there are only 9 digits in 1 through 9 (inclusive) so a digit would have
    to repeat at least one time, and the result would not be pandigital.
"""    

from util import repeatsDigits

def p38():
    max_pandigital=0
    for i in xrange(1,9999):
        temp=str(i)
        counter=2
        if '0' in temp or repeatsDigits(temp):
            continue
        while len(temp) < 9:
            temp+=str(counter*i)
        if len(temp) != 9 or '0' in temp or repeatsDigits(temp):
            continue
        max_pandigital=max(max_pandigital, int(temp))
    print max_pandigital 
p38() 
