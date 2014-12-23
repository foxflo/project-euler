#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def p2(limit=4000000):
    a,b=1,1
    value = 0
    while a < limit and b < limit:
        a+=b
        b+=a
        if a%2==0:
            value += a
        elif b%2==0:
            value += b
    print value
p2()
