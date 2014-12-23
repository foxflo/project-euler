#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def p6(x=100):
    sum_squares=0
    for i in xrange(x+1):
        sum_squares+=i*i
    square_sum=x*(x+1)/2*x*(x+1)/2
    print square_sum-sum_squares
p6(100)
