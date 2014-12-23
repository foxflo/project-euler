#Find the sum of the digits in the number 100!

def p20(n=100):
    fac=1
    for i in xrange(1,n+1):
        fac*=i
    total=0
    for i in str(fac):
        total+=int(i)
    print total
p20()
