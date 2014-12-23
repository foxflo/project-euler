#How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

def p53(lower=1,upper=100,n=1000000):
    factorials=[reduce(lambda a,b:a*b, range(i)[1:],1) for i in xrange(upper+1)]  #precompute factorials
    count=0
    for i in xrange(lower,upper+1):
        for j in xrange(i/2):
            if factorials[i]/(factorials[j]*factorials[i-j]) > n:
                count+=2
                if i%2==0:
                    count-=1
    print count
p53()
