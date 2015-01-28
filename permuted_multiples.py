#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def p52(n=6):
    counter=1
    while True:
        for i in xrange(1,n+1):
            if len(set(str(counter)).symmetric_difference(set(str(counter*i)))):
                break
            if i==n:
                print counter
                return
        counter+=1
p52()
