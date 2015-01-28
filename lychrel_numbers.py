#How many Lychrel numbers are there below ten-thousand?

from util import isPalin

def p55(n=10000):
    counter=0
    for i in xrange(1,n):
        temp=i
        for j in xrange(50):
            temp+=int(str(temp)[::-1])
            if isPalin(str(temp)):
                counter+=1
                break
    print n-1-counter
p55()
