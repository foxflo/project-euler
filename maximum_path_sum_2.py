#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

""" This is the same algorithm as problem 18, namely the dynamic programming approach. 
    Code is reproduced below for ease of use.
"""

def p67(triangle="p67.triangle"):
    triangle=open(triangle)
    numbers=triangle.read().split('\n')
    triangle.close()
    triangle=[]
    for row in numbers[:-1]:
        triangle.append(row.split())
    for i in xrange(len(triangle)):
        for j in xrange(len(triangle[i])):
            triangle[i][j]=int(triangle[i][j])
    sums=triangle[0]
    tempsums=[None]*2
    for i in xrange(1,len(triangle[1:])+1):
        for j in xrange(len(triangle[i])):
            if j==0:
                tempsums[0]=sums[0]+triangle[i][0]
            elif j==len(triangle[i])-1:
                tempsums[-1]=sums[j-1]+triangle[i][j]
            else:
                tempsums[j]=max(sums[j-1]+triangle[i][j],sums[j]+triangle[i][j])
        sums=tempsums
        tempsums=[None]*(len(triangle[i])+1)
    print max(sums)
p67()
