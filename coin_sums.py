#How many different ways can 200p be made using any number of coins?

coin_values=[2,5,10,20,50,100,200]

def p31(n=200):
    x=[1]*(n+1)
    counter=0
    for i in coin_values:
        for j in xrange(n+1):
            if i > j:
                continue
            x[j]+=x[j-i]
    print x[-1]
p31()
