#Find the last ten digits of this prime number. 28433*2^7830457+1.

def p97(base=2,exponent=7830457,factor=28433):
    counter=0
    current=1
    while counter < exponent:
        counter+=1
        current*=base
        current%=10**10
    current=factor*current+1
    print str(current)[-10:]
p97()
