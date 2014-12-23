#How many such routes are there through a 20x20 grid?

""" Note that this is actually just pascal's triangle since the number of ways to reach any point is the sum 
    of the number of ways to reach the point above and to the left of it. This is analogous to pascal's triangle
    if we just turn the grid diagonally, so square 1,1 is on top. Since the number of ways to reach any point on
    the top or left edges is just 1 and the rest are appropriate sums. Then, to find the number of ways, we just 
    need to calculate the value of pascall's triangle at the corresponding location.
    
    We have a closed form for pascal's triangle, yay!
"""

from util import choose

def p15(n=20, m=20):
    print choose(n+n,n)
p15()
