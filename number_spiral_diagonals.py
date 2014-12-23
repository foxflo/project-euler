#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

""" Note that the distance between corners increases by 2 every time the size of the square increases.
    Furthermore, aside from 1, there are 4 numbers to sum for each time the square increases in size.
    
    Then the answer in general is: 1+(4*1+2*10)+(4*9+4*10)+... = 1+sum(n=1 to n/2) (4*(2n-1)^2+20n)
"""

def p28(n=1001):
    print 1+sum([16*i*i+4*i+4 for i in xrange(1,n/2+1)])
p28()
