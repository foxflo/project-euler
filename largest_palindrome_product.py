#Find the largest palindrome made from the product of two 3-digit numbers.

def p4():
    palins=[]
    for i in xrange(999,99,-1):
        for j in xrange(999,99,-1):
            if str(i*j)==str(i*j)[::-1]:
                palins.append(i*j)
    largest=0
    for i in palins:
        largest=max(largest,i)
    print largest
p4()
