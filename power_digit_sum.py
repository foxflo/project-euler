#What is the sum of the digits of the number 2^1000?

""" Again, this is easy because python has arbitrary precision integers implicitly built in.
"""

def p16(base=2,exp=1000):
    number=str(base**exp)
    total=0
    for i in xrange(len(number)):
        total+=int(number[i])
    print total
p16()
