#Find the next triangle number that is also pentagonal and hexagonal.

""" It would be computationally expensive to compute and keep around lists of triangular, pentagonal, and 
    hexagonal numbers. 
    
    Furthermore, hexagonal numbers grow the quickest so we'll check those instead of anything else since we'll
    have fewer terms to check. 
    
    Once we find the second hexagonal number which is also triangular and pentagonal, we will have found the 
    next triangular number that is also hexagonal and pentagonal.
"""

from util import isPentagonal,isTriangular

def p45():
    hexag=144
    while True:
        hexagNum=hexag*(2*hexag-1)
        if isTriangular(hexagNum) and isPentagonal(hexagNum):
            print hexagNum
            return
        hexag+=1
p45()
