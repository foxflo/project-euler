#If d_n represents the nth digit of the fractional part, find the value of the following expression. d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000

""" Notice the pattern: the first 9 integers>0 have a single digit. The next 90 integers have two digits. 
    The next 900 integers have three digits. etc.
"""

def get_digit_champernowne(n):
    current_length=1
    counter=9
    while counter < n:
        current_length+=1
        counter+=current_length*9*10**(current_length-1)
    coarse_distance=(counter-n)/current_length
    remainder=(counter-n)%current_length
    upper=10**current_length-1-coarse_distance
    return int(str(upper)[-(remainder+1)])

def p40(n=[1,10,100,1000,10000,100000,1000000]):
    print reduce(lambda a,b:a*b, [get_digit_champernowne(i) for i in n])

p40()
