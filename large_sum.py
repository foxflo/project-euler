#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

""" Since python does implicit upcasting to large integer formats, we can just ask it to compute directly
    In other languages that do not do this (java, for example) we'd either need to:
        explicitly represent the numbers as bigintegers (java's arbitrary precision integer class)
    or be clever:
        consider only the first 11 numbers 
"""

def p13(n=10):
    nums=open("p13.numbers")
    list_nums=nums.read().split()
    nums.close()
    for i in xrange(len(list_nums)):
        list_nums[i]=int(list_nums[i])
    print str(sum(list_nums))[:n] 
p13()
